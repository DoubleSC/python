"""
매매 전략

여기 있는 함수들은 증권사 API 와 상관없이 "숫자만 받아서 판단"합니다.
그래서 실제 돈 없이도 테스트할 수 있습니다. (tests/test_strategy.py 참고)
"""

BUY = "BUY"
SELL = "SELL"
HOLD = "HOLD"


def moving_average(prices, n):
    """최근 n 개 가격의 평균. 데이터가 부족하면 None"""
    if len(prices) < n:
        return None
    return sum(prices[-n:]) / n


def ma_cross_signal(closes, short=5, long=20):
    """
    이동평균선 골든크로스 / 데드크로스 전략

    - 골든크로스: 단기 평균선이 장기 평균선을 아래 -> 위로 뚫음  => 매수(BUY)
    - 데드크로스: 단기 평균선이 장기 평균선을 위 -> 아래로 뚫음  => 매도(SELL)
    - 그 외                                                     => 관망(HOLD)

    closes: 종가 리스트 (오래된 것 -> 최근 것)
    """
    if short >= long:
        raise ValueError("short 는 long 보다 작아야 합니다.")
    if len(closes) < long + 1:
        return HOLD  # 어제와 오늘 장기 평균을 모두 계산할 만큼 데이터가 필요

    today_short = moving_average(closes, short)
    today_long = moving_average(closes, long)
    yday_short = moving_average(closes[:-1], short)
    yday_long = moving_average(closes[:-1], long)

    if yday_short <= yday_long and today_short > today_long:
        return BUY
    if yday_short >= yday_long and today_short < today_long:
        return SELL
    return HOLD


def check_stop(avg_price, current_price, stop_loss_pct, take_profit_pct):
    """
    손절 / 익절 체크
    - 수익률이 -stop_loss_pct% 이하면 SELL (손절)
    - 수익률이 +take_profit_pct% 이상이면 SELL (익절)
    """
    if avg_price <= 0:
        return HOLD
    rate = (current_price - avg_price) / avg_price * 100
    if rate <= -stop_loss_pct or rate >= take_profit_pct:
        return SELL
    return HOLD


def calc_buy_qty(budget, price):
    """예산(원) 안에서 살 수 있는 최대 수량"""
    if price <= 0:
        return 0
    return int(budget // price)
