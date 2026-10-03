"""
주식 매매 프로그램 실행 파일

사용법 (stock_trader 폴더에서 실행):
    python main.py price 005930            # 현재가 조회
    python main.py balance                 # 잔고 조회
    python main.py buy 005930 1            # 시장가 1주 매수
    python main.py buy 005930 1 70000      # 70,000원 지정가 1주 매수
    python main.py sell 005930 1           # 시장가 1주 매도
    python main.py signal 005930           # 이동평균 전략 신호만 확인
    python main.py auto                    # 자동매매 시작 (Ctrl+C 로 종료)
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime, time as dtime

from kis_api import KISClient, KISError
from strategy import BUY, SELL, HOLD, ma_cross_signal, check_stop, calc_buy_qty

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(BASE_DIR, "config.json")

MARKET_OPEN = dtime(9, 0)
MARKET_CLOSE = dtime(15, 20)  # 장 마감(15:30) 10분 전까지만 매매


def load_config():
    if not os.path.exists(CONFIG_FILE):
        print("config.json 이 없습니다. config.example.json 을 복사해서 만들어 주세요.")
        print("  예) cp config.example.json config.json")
        sys.exit(1)
    with open(CONFIG_FILE, encoding="utf-8") as f:
        return json.load(f)


def make_client(cfg):
    return KISClient(cfg["app_key"], cfg["app_secret"], cfg["account_no"],
                     paper=cfg.get("paper", True))


def log(msg):
    print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {msg}")


# ----------------------------------------------------------------------
# 수동 명령
# ----------------------------------------------------------------------
def cmd_price(client, args):
    p = client.get_price(args.code)
    print(f"{p['code']} 현재가 {p['price']:,}원 "
          f"({p['change']:+,}원, {p['change_rate']:+.2f}%) 거래량 {p['volume']:,}")


def cmd_balance(client, args):
    b = client.get_balance()
    print(f"예수금: {b['cash']:,}원 / 총평가: {b['total_eval']:,}원")
    if not b["holdings"]:
        print("보유 종목 없음")
    for h in b["holdings"]:
        print(f"  {h['name']}({h['code']}) {h['qty']}주 "
              f"평균 {h['avg_price']:,.0f}원 -> 현재 {h['price']:,}원 ({h['profit_rate']:+.2f}%)")


def cmd_order(client, args, cfg):
    side = args.command  # "buy" 또는 "sell"
    kind = "시장가" if args.price == 0 else f"{args.price:,}원 지정가"
    mode = "모의투자" if client.paper else "★실전투자★"
    print(f"[{mode}] {args.code} {args.qty}주 {kind} {'매수' if side == 'buy' else '매도'}")

    # 실전투자일 때는 한 번 더 확인
    if not client.paper:
        if input("정말 주문할까요? (yes 입력): ").strip().lower() != "yes":
            print("취소했습니다.")
            return
    order_no = client.order(side, args.code, args.qty, args.price)
    print(f"주문 완료! 주문번호: {order_no}")


def cmd_signal(client, args, cfg):
    a = cfg.get("auto", {})
    closes = client.get_daily_closes(args.code)
    sig = ma_cross_signal(closes, a.get("short_ma", 5), a.get("long_ma", 20))
    print(f"{args.code} 최근 종가 {closes[-1]:,}원 -> 신호: {sig}")


# ----------------------------------------------------------------------
# 자동매매
# ----------------------------------------------------------------------
def is_market_time(now=None):
    now = now or datetime.now()
    if now.weekday() >= 5:  # 토(5), 일(6)
        return False
    return MARKET_OPEN <= now.time() <= MARKET_CLOSE


def run_once(client, a):
    """감시 종목을 한 바퀴 돌면서 매수/매도 판단"""
    dry_run = a.get("dry_run", True)
    balance = client.get_balance()
    holdings = {h["code"]: h for h in balance["holdings"]}

    for code in a["watch_list"]:
        try:
            closes = client.get_daily_closes(code)
            price = client.get_price(code)["price"]
            signal = ma_cross_signal(closes, a.get("short_ma", 5), a.get("long_ma", 20))
            held = holdings.get(code)

            # 1) 보유 중이면: 손절/익절 또는 데드크로스 시 매도
            if held:
                stop = check_stop(held["avg_price"], price,
                                  a.get("stop_loss_pct", 5), a.get("take_profit_pct", 10))
                if stop == SELL or signal == SELL:
                    reason = "손절/익절" if stop == SELL else "데드크로스"
                    log(f"{code} 매도 신호({reason}) {held['qty']}주 @ {price:,}")
                    if not dry_run:
                        log(f"  -> 주문번호 {client.sell(code, held['qty'])}")
                    continue

            # 2) 미보유면: 골든크로스 시 예산 안에서 매수
            if not held and signal == BUY:
                qty = calc_buy_qty(min(a["budget_per_stock"], balance["cash"]), price)
                if qty == 0:
                    log(f"{code} 매수 신호지만 예산 부족")
                    continue
                log(f"{code} 매수 신호(골든크로스) {qty}주 @ {price:,}")
                if not dry_run:
                    log(f"  -> 주문번호 {client.buy(code, qty)}")
                    balance["cash"] -= qty * price
                continue

            log(f"{code} {price:,}원 -> {HOLD}")
        except KISError as e:
            log(f"{code} 처리 중 API 오류: {e}")


def cmd_auto(client, args, cfg):
    a = cfg["auto"]
    mode = "모의투자" if client.paper else "★실전투자★"
    log(f"자동매매 시작 [{mode}] dry_run={a.get('dry_run', True)} 감시종목={a['watch_list']}")
    if a.get("dry_run", True):
        log("dry_run 모드: 신호만 출력하고 실제 주문은 넣지 않습니다.")

    try:
        while True:
            if is_market_time():
                run_once(client, a)
            else:
                log("장 운영 시간이 아닙니다. 대기 중...")
            time.sleep(a.get("interval_sec", 60))
    except KeyboardInterrupt:
        log("자동매매 종료")


# ----------------------------------------------------------------------
def build_parser():
    parser = argparse.ArgumentParser(description="한국투자증권 API 주식 매매 프로그램")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("price", help="현재가 조회")
    p.add_argument("code", help="종목코드 6자리")

    sub.add_parser("balance", help="잔고 조회")

    for name, help_text in (("buy", "매수"), ("sell", "매도")):
        p = sub.add_parser(name, help=help_text)
        p.add_argument("code", help="종목코드 6자리")
        p.add_argument("qty", type=int, help="수량")
        p.add_argument("price", type=int, nargs="?", default=0, help="지정가 (생략하면 시장가)")

    p = sub.add_parser("signal", help="이동평균 전략 신호 확인")
    p.add_argument("code", help="종목코드 6자리")

    sub.add_parser("auto", help="자동매매 시작")
    return parser


def main():
    args = build_parser().parse_args()
    cfg = load_config()
    client = make_client(cfg)

    try:
        if args.command == "price":
            cmd_price(client, args)
        elif args.command == "balance":
            cmd_balance(client, args)
        elif args.command in ("buy", "sell"):
            cmd_order(client, args, cfg)
        elif args.command == "signal":
            cmd_signal(client, args, cfg)
        elif args.command == "auto":
            cmd_auto(client, args, cfg)
    except KISError as e:
        print(f"API 오류: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
