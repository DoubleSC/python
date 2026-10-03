# 주식 자동매매 프로그램 (한국투자증권 Open API)

한국투자증권 **KIS Developers Open API**(REST 방식)로 시세 조회, 잔고 조회, 매수/매도, 자동매매를 하는 파이썬 프로그램입니다.
Windows, Mac, Linux 어디서나 돌아가고, **모의투자**로 먼저 연습할 수 있습니다.

## 파일 구성

| 파일 | 역할 |
|---|---|
| `kis_api.py` | 증권사 서버와 통신 (토큰 발급, 시세, 잔고, 주문) |
| `strategy.py` | 매매 전략 (이동평균 골든/데드크로스, 손절·익절) |
| `main.py` | 실행 파일 (명령어 처리, 자동매매 루프) |
| `config.example.json` | 설정 예시 → `config.json` 으로 복사해서 사용 |
| `tests/` | 전략 및 주문 테스트 (계정 없이 실행 가능) |

## 1. API 키 발급 받기

1. 한국투자증권 계좌를 만듭니다. (비대면 개설 가능)
2. [KIS Developers](https://apiportal.koreainvestment.com)에서 **API 신청**을 합니다.
3. 처음에는 **모의투자** 계좌를 신청해서 모의투자용 `APP KEY` / `APP SECRET`을 받으세요.

## 2. 설치

```bash
pip install requests
cd stock_trader
cp config.example.json config.json   # Windows: copy config.example.json config.json
```

`config.json`을 열어서 `app_key`, `app_secret`, `account_no`(예: `50012345-01`)를 채웁니다.

> ⚠️ `config.json`에는 비밀키가 들어 있습니다. `.gitignore`로 막아 두었으니 **절대 깃허브에 올리지 마세요.**

## 3. 사용법

```bash
python main.py price 005930          # 삼성전자 현재가
python main.py balance               # 내 잔고
python main.py buy 005930 1          # 시장가 1주 매수
python main.py buy 005930 1 70000    # 70,000원 지정가 1주 매수
python main.py sell 005930 1         # 시장가 1주 매도
python main.py signal 005930         # 전략 신호(BUY/SELL/HOLD) 확인
python main.py auto                  # 자동매매 시작 (Ctrl+C로 종료)
```

## 4. 자동매매 전략

`config.json`의 `auto` 설정:

| 항목 | 의미 | 기본값 |
|---|---|---|
| `dry_run` | `true`면 신호만 출력하고 주문은 넣지 않음 | `true` |
| `watch_list` | 감시할 종목코드 목록 | 삼성전자, SK하이닉스 |
| `budget_per_stock` | 종목당 최대 매수 금액(원) | 500,000 |
| `short_ma` / `long_ma` | 단기/장기 이동평균 일수 | 5 / 20 |
| `stop_loss_pct` | 손절 기준(%) | 5 |
| `take_profit_pct` | 익절 기준(%) | 10 |
| `interval_sec` | 몇 초마다 확인할지 | 60 |

동작 방식 (평일 09:00~15:20에만 동작):
- **안 가진 종목** → 5일선이 20일선을 위로 뚫으면(골든크로스) 예산만큼 **매수**
- **가진 종목** → 5일선이 20일선을 아래로 뚫거나(데드크로스), 손절/익절 기준에 닿으면 전량 **매도**

전략을 바꾸고 싶다면 `strategy.py`에 함수를 추가하고 `main.py`의 `run_once()`에서 호출하면 됩니다.

## 5. 테스트

```bash
python -m unittest discover tests
```

## 안전하게 쓰는 순서

1. `paper: true`, `dry_run: true` → 신호가 잘 나오는지 확인
2. `paper: true`, `dry_run: false` → 모의투자로 실제 주문 연습
3. 충분히 검증한 뒤에만 실전 키로 바꾸고 `paper: false` (실전에서 수동 주문할 때는 `yes`를 한 번 더 입력해야 주문됨)

> 이 프로그램은 학습용 예제입니다. 투자 손실에 대한 책임은 본인에게 있습니다.
