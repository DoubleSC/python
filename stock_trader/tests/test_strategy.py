"""
전략 테스트 (증권사 계정 없이 실행 가능)

stock_trader 폴더에서:
    python -m unittest discover tests
"""

import os
import sys
import unittest
from datetime import datetime
from unittest.mock import MagicMock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from strategy import BUY, SELL, HOLD, moving_average, ma_cross_signal, check_stop, calc_buy_qty
from kis_api import KISClient
import main


class TestStrategy(unittest.TestCase):
    def test_moving_average(self):
        self.assertEqual(moving_average([1, 2, 3, 4, 5], 5), 3)
        self.assertEqual(moving_average([1, 2, 3, 4, 5], 2), 4.5)
        self.assertIsNone(moving_average([1, 2], 5))

    def test_golden_cross(self):
        # 계속 떨어지다가 마지막 날 급등 -> 단기선이 장기선을 위로 뚫음
        closes = list(range(130, 109, -1)) + [200]
        self.assertEqual(ma_cross_signal(closes, 5, 20), BUY)

    def test_dead_cross(self):
        closes = list(range(100, 121)) + [10]
        self.assertEqual(ma_cross_signal(closes, 5, 20), SELL)

    def test_hold(self):
        self.assertEqual(ma_cross_signal([100] * 30, 5, 20), HOLD)
        self.assertEqual(ma_cross_signal([100] * 5, 5, 20), HOLD)  # 데이터 부족

    def test_stop(self):
        self.assertEqual(check_stop(10000, 9400, 5, 10), SELL)    # -6% 손절
        self.assertEqual(check_stop(10000, 11100, 5, 10), SELL)   # +11% 익절
        self.assertEqual(check_stop(10000, 10300, 5, 10), HOLD)

    def test_buy_qty(self):
        self.assertEqual(calc_buy_qty(500000, 70000), 7)
        self.assertEqual(calc_buy_qty(50000, 70000), 0)


class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = KISClient("key", "secret", "12345678-01", paper=True)
        self.client._token = "TOKEN"
        self.client._token_expire = datetime(2999, 1, 1)
        self.client.session = MagicMock()
        self.client.session.request.return_value.json.return_value = {
            "rt_cd": "0", "output": {"ODNO": "0000123"},
        }

    def test_bad_account(self):
        with self.assertRaises(ValueError):
            KISClient("k", "s", "1234")

    def test_paper_buy_market_order(self):
        self.assertEqual(self.client.buy("005930", 3), "0000123")
        kwargs = self.client.session.request.call_args.kwargs
        self.assertEqual(kwargs["headers"]["tr_id"], "VTTC0012U")
        self.assertEqual(kwargs["json"]["ORD_DVSN"], "01")
        self.assertEqual(kwargs["json"]["ORD_QTY"], "3")
        self.assertEqual(kwargs["json"]["CANO"], "12345678")

    def test_limit_sell(self):
        self.client.sell("005930", 1, 70000)
        kwargs = self.client.session.request.call_args.kwargs
        self.assertEqual(kwargs["headers"]["tr_id"], "VTTC0011U")
        self.assertEqual(kwargs["json"]["ORD_DVSN"], "00")
        self.assertEqual(kwargs["json"]["ORD_UNPR"], "70000")


class TestMarketTime(unittest.TestCase):
    def test_market_time(self):
        self.assertTrue(main.is_market_time(datetime(2026, 10, 5, 10, 0)))    # 월요일 10시
        self.assertFalse(main.is_market_time(datetime(2026, 10, 5, 8, 59)))
        self.assertFalse(main.is_market_time(datetime(2026, 10, 4, 10, 0)))   # 일요일


if __name__ == "__main__":
    unittest.main()
