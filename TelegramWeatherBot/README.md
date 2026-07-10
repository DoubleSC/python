# 텔레그램 날씨 알림 봇

매일 새벽 6시에 현재 위치의 오늘 날씨 예보(최저/최고 기온, 강수 확률, 날씨 상태)를
텔레그램으로 보내주는 봇입니다.

## 1. 준비물

1. **텔레그램 봇 토큰**
   - 텔레그램에서 `@BotFather`와 대화 시작 → `/newbot` → 안내에 따라 봇 생성
   - 발급받은 토큰을 `TELEGRAM_BOT_TOKEN`에 입력

2. **채팅 ID**
   - 만든 봇과 먼저 대화방에서 아무 메시지나 전송
   - 브라우저로 `https://api.telegram.org/bot<토큰>/getUpdates` 접속
   - 응답 JSON에서 `message.chat.id` 값을 확인해 `TELEGRAM_CHAT_ID`에 입력

3. **OpenWeatherMap API 키**
   - https://openweathermap.org/ 가입 후 API keys 메뉴에서 발급
   - `OPENWEATHER_API_KEY`에 입력 (발급 직후에는 활성화까지 몇 분 걸릴 수 있음)

4. **위치 설정 (선택, 권장)**
   - 기본값은 서버가 접속된 공인 IP를 기준으로 위치를 추정합니다(`ip-api.com`).
     클라우드 서버 등 실제 거주지와 IP 위치가 다른 환경이면 부정확할 수 있습니다.
   - 정확한 위치를 원하면 `.env`의 `WEATHER_LAT`, `WEATHER_LON`, `WEATHER_CITY_NAME`에
     원하는 좌표와 지역명을 직접 입력하세요. (좌표는 지도 서비스에서 쉽게 확인 가능)

## 2. 설치

```bash
cd TelegramWeatherBot
pip install -r requirements.txt
cp .env.example .env
# .env 파일을 열어 토큰, 채팅 ID, API 키 등을 입력
```

## 3. 실행

즉시 한 번 테스트 전송:

```bash
python weather_bot.py --now
```

매일 06:00 자동 전송 (프로세스를 계속 띄워둬야 함):

```bash
python weather_bot.py
```

## 4. 서버에서 계속 실행하기

### 방법 A: crontab (권장)

스케줄러를 직접 돌리는 대신, cron이 매일 06:00에 `--now` 옵션으로 스크립트를
한 번만 실행하도록 등록하면 프로세스를 상시 띄워둘 필요가 없습니다.

```bash
crontab -e
```

아래 줄 추가 (경로는 실제 설치 위치로 수정):

```
0 6 * * * cd /path/to/TelegramWeatherBot && /usr/bin/python3 weather_bot.py --now >> weather_bot.log 2>&1
```

### 방법 B: 스크립트 자체 스케줄러

`python weather_bot.py`를 `nohup`, `tmux`, `systemd` 서비스 등으로 백그라운드에
계속 실행해두면 내부 스케줄러가 매일 06:00에 자동으로 전송합니다.

```bash
nohup python weather_bot.py > weather_bot.log 2>&1 &
```
