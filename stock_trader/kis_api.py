"""
한국투자증권(KIS) Open API 클라이언트

- 공식 문서: https://apiportal.koreainvestment.com
- 공식 예제: https://github.com/koreainvestment/open-trading-api

이 파일은 "증권사 서버와 대화하는 부분"만 담당합니다.
(언제 사고 팔지는 strategy.py, 프로그램 실행은 main.py 가 담당)
"""

import json
import os
import time
from datetime import datetime, timedelta

import requests

# 실전투자 / 모의투자 서버 주소
REAL_URL = "https://openapi.koreainvestment.com:9443"
PAPER_URL = "https://openapivts.koreainvestment.com:29443"

# 거래 ID(tr_id): API 마다 정해진 이름. 모의투자는 맨 앞 글자가 T -> V 로 바뀝니다.
# (주문 tr_id 는 2024년에 TTTC0802U/0801U -> TTTC0012U/0011U 로 변경되었습니다)
TR_ID = {
    "price": ("FHKST01010100", "FHKST01010100"),        # 현재가 조회 (실전, 모의)
    "daily": ("FHKST01010400", "FHKST01010400"),        # 일별 시세 조회
    "balance": ("TTTC8434R", "VTTC8434R"),              # 잔고 조회
    "buy": ("TTTC0012U", "VTTC0012U"),                  # 현금 매수 주문
    "sell": ("TTTC0011U", "VTTC0011U"),                 # 현금 매도 주문
}

TOKEN_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".token_cache.json")


class KISError(Exception):
    """증권사 API 가 오류를 돌려줬을 때 발생시키는 예외"""


class KISClient:
    def __init__(self, app_key, app_secret, account_no, paper=True, timeout=10):
        """
        app_key, app_secret : KIS Developers 에서 발급받은 키
        account_no          : 계좌번호 "12345678-01" 형식
        paper               : True 면 모의투자, False 면 실전투자
        """
        self.app_key = app_key
        self.app_secret = app_secret
        self.paper = paper
        self.base_url = PAPER_URL if paper else REAL_URL
        self.timeout = timeout

        # 계좌번호는 앞 8자리(CANO) + 뒤 2자리(상품코드) 로 나눠서 보냅니다.
        cano, _, prdt = account_no.partition("-")
        if len(cano) != 8 or len(prdt) != 2:
            raise ValueError("계좌번호는 '12345678-01' 형식으로 입력하세요.")
        self.cano = cano
        self.acnt_prdt_cd = prdt

        self.session = requests.Session()
        self._token = None
        self._token_expire = None

    # ------------------------------------------------------------------
    # 인증 토큰
    # ------------------------------------------------------------------
    def _load_cached_token(self):
        """토큰은 1분에 1번만 발급 가능하므로 파일에 저장해 두고 재사용합니다."""
        try:
            with open(TOKEN_FILE, encoding="utf-8") as f:
                data = json.load(f)
        except (OSError, ValueError):
            return False
        if data.get("app_key") != self.app_key or data.get("paper") != self.paper:
            return False
        expire = datetime.fromisoformat(data["expire"])
        if expire - datetime.now() < timedelta(minutes=10):  # 만료 10분 전이면 새로 발급
            return False
        self._token = data["token"]
        self._token_expire = expire
        return True

    def _issue_token(self):
        url = f"{self.base_url}/oauth2/tokenP"
        body = {
            "grant_type": "client_credentials",
            "appkey": self.app_key,
            "appsecret": self.app_secret,
        }
        res = self.session.post(url, json=body, timeout=self.timeout)
        data = res.json()
        if "access_token" not in data:
            raise KISError(f"토큰 발급 실패: {data}")

        self._token = data["access_token"]
        self._token_expire = datetime.now() + timedelta(seconds=int(data.get("expires_in", 86400)))
        try:
            with open(TOKEN_FILE, "w", encoding="utf-8") as f:
                json.dump({
                    "app_key": self.app_key,
                    "paper": self.paper,
                    "token": self._token,
                    "expire": self._token_expire.isoformat(),
                }, f)
        except OSError:
            pass  # 저장 실패해도 이번 실행에서는 문제 없음

    def get_token(self):
        if self._token and self._token_expire - datetime.now() > timedelta(minutes=10):
            return self._token
        if not self._load_cached_token():
            self._issue_token()
        return self._token

    # ------------------------------------------------------------------
    # 공통 요청 함수
    # ------------------------------------------------------------------
    def _tr_id(self, name):
        real, paper = TR_ID[name]
        return paper if self.paper else real

    def _request(self, method, path, tr_id, params=None, body=None):
        headers = {
            "content-type": "application/json; charset=utf-8",
            "authorization": f"Bearer {self.get_token()}",
            "appkey": self.app_key,
            "appsecret": self.app_secret,
            "tr_id": tr_id,
            "custtype": "P",  # 개인
        }
        url = f"{self.base_url}{path}"
        res = self.session.request(method, url, headers=headers, params=params,
                                   json=body, timeout=self.timeout)
        data = res.json()

        # rt_cd 가 "0" 이면 성공, 그 외는 실패
        if data.get("rt_cd") != "0":
            raise KISError(f"[{data.get('msg_cd')}] {data.get('msg1')}")

        # 모의투자 서버는 초당 요청 수 제한이 빡빡해서 살짝 쉬어줍니다.
        time.sleep(0.5 if self.paper else 0.06)
        return data

    # ------------------------------------------------------------------
    # 시세 조회
    # ------------------------------------------------------------------
    def get_price(self, code):
        """현재가 조회. code 는 종목코드 6자리 (예: 삼성전자 '005930')"""
        data = self._request(
            "GET",
            "/uapi/domestic-stock/v1/quotations/inquire-price",
            self._tr_id("price"),
            params={"FID_COND_MRKT_DIV_CODE": "J", "FID_INPUT_ISCD": code},
        )
        out = data["output"]
        return {
            "code": code,
            "price": int(out["stck_prpr"]),          # 현재가
            "change": int(out["prdy_vrss"]),         # 전일 대비
            "change_rate": float(out["prdy_ctrt"]),  # 등락률(%)
            "volume": int(out["acml_vol"]),          # 누적 거래량
        }

    def get_daily_closes(self, code):
        """최근 30거래일 종가 리스트 (오래된 날 -> 최근 날 순서)"""
        data = self._request(
            "GET",
            "/uapi/domestic-stock/v1/quotations/inquire-daily-price",
            self._tr_id("daily"),
            params={
                "FID_COND_MRKT_DIV_CODE": "J",
                "FID_INPUT_ISCD": code,
                "FID_PERIOD_DIV_CODE": "D",  # D: 일, W: 주, M: 월
                "FID_ORG_ADJ_PRC": "0",      # 0: 수정주가 반영
            },
        )
        rows = [r for r in data["output"] if r.get("stck_clpr")]
        rows.reverse()  # API 는 최근 날짜부터 주므로 뒤집기
        return [int(r["stck_clpr"]) for r in rows]

    # ------------------------------------------------------------------
    # 계좌
    # ------------------------------------------------------------------
    def get_balance(self):
        """보유 종목과 예수금 조회"""
        data = self._request(
            "GET",
            "/uapi/domestic-stock/v1/trading/inquire-balance",
            self._tr_id("balance"),
            params={
                "CANO": self.cano,
                "ACNT_PRDT_CD": self.acnt_prdt_cd,
                "AFHR_FLPR_YN": "N",
                "OFL_YN": "",
                "INQR_DVSN": "02",
                "UNPR_DVSN": "01",
                "FUND_STTL_ICLD_YN": "N",
                "FNCG_AMT_AUTO_RDPT_YN": "N",
                "PRCS_DVSN": "00",
                "CTX_AREA_FK100": "",
                "CTX_AREA_NK100": "",
            },
        )
        holdings = []
        for h in data["output1"]:
            qty = int(h["hldg_qty"])
            if qty == 0:
                continue
            holdings.append({
                "code": h["pdno"],
                "name": h["prdt_name"],
                "qty": qty,
                "avg_price": float(h["pchs_avg_pric"]),
                "price": int(h["prpr"]),
                "profit_rate": float(h["evlu_pfls_rt"]),
            })
        summary = data["output2"][0] if data["output2"] else {}
        return {
            "holdings": holdings,
            "cash": int(summary.get("dnca_tot_amt", 0)),          # 예수금
            "total_eval": int(summary.get("tot_evlu_amt", 0)),    # 총 평가금액
        }

    # ------------------------------------------------------------------
    # 주문
    # ------------------------------------------------------------------
    def order(self, side, code, qty, price=0):
        """
        side  : "buy" 또는 "sell"
        qty   : 주문 수량
        price : 0 이면 시장가, 0 보다 크면 지정가
        반환값: 주문번호
        """
        if side not in ("buy", "sell"):
            raise ValueError("side 는 'buy' 또는 'sell' 이어야 합니다.")
        if qty <= 0:
            raise ValueError("수량은 1 이상이어야 합니다.")

        body = {
            "CANO": self.cano,
            "ACNT_PRDT_CD": self.acnt_prdt_cd,
            "PDNO": code,
            "ORD_DVSN": "01" if price == 0 else "00",  # 01: 시장가, 00: 지정가
            "ORD_QTY": str(qty),                        # 숫자도 문자열로 보내야 함
            "ORD_UNPR": str(price),
        }
        data = self._request(
            "POST",
            "/uapi/domestic-stock/v1/trading/order-cash",
            self._tr_id(side),
            body=body,
        )
        return data["output"]["ODNO"]

    def buy(self, code, qty, price=0):
        return self.order("buy", code, qty, price)

    def sell(self, code, qty, price=0):
        return self.order("sell", code, qty, price)
