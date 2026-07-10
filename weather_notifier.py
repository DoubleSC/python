"""매일 아침 6시에 오늘의 날씨를 알려주는 프로그램."""

import time
from datetime import datetime, timedelta

import requests

CITY = "Seoul"
NOTIFY_HOUR = 6
NOTIFY_MINUTE = 0


def get_weather(city: str) -> str:
    response = requests.get(
        f"https://wttr.in/{city}", params={"format": "4", "lang": "ko"}, timeout=10
    )
    response.raise_for_status()
    return response.text.strip()


def notify(message: str) -> None:
    print(f"[{datetime.now():%Y-%m-%d %H:%M}] {message}")


def seconds_until_next_run(hour: int, minute: int) -> float:
    now = datetime.now()
    next_run = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if next_run <= now:
        next_run += timedelta(days=1)
    return (next_run - now).total_seconds()


def main() -> None:
    print(f"날씨 알리미 시작: 매일 {NOTIFY_HOUR:02d}:{NOTIFY_MINUTE:02d}에 '{CITY}' 날씨를 알려드립니다.")
    while True:
        time.sleep(seconds_until_next_run(NOTIFY_HOUR, NOTIFY_MINUTE))
        try:
            notify(f"오늘의 날씨: {get_weather(CITY)}")
        except requests.RequestException as e:
            notify(f"날씨 정보를 가져오지 못했습니다: {e}")


if __name__ == "__main__":
    main()
