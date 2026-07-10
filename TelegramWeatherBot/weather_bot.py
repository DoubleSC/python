import os
import sys
import time
from datetime import datetime

import requests
import schedule
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
FIXED_LAT = os.getenv("WEATHER_LAT")
FIXED_LON = os.getenv("WEATHER_LON")
FIXED_CITY_NAME = os.getenv("WEATHER_CITY_NAME", "설정된 위치")


def get_current_location():
    if FIXED_LAT and FIXED_LON:
        return float(FIXED_LAT), float(FIXED_LON), FIXED_CITY_NAME

    response = requests.get("http://ip-api.com/json/", timeout=10)
    response.raise_for_status()
    data = response.json()
    if data.get("status") != "success":
        raise RuntimeError(f"위치 조회 실패: {data.get('message', 'unknown error')}")
    return data["lat"], data["lon"], data.get("city", "현재 위치")


def get_today_forecast(lat, lon):
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",
        "lang": "kr",
    }
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    today = datetime.now().date()
    todays_entries = [
        entry for entry in data["list"]
        if datetime.fromtimestamp(entry["dt"]).date() == today
    ]
    if not todays_entries:
        # 자정 무렵 등 오늘자 데이터가 없으면 가장 가까운 예보로 대체
        todays_entries = data["list"][:4]

    temps = [entry["main"]["temp"] for entry in todays_entries]
    pops = [entry.get("pop", 0) for entry in todays_entries]
    descriptions = [entry["weather"][0]["description"] for entry in todays_entries]

    return {
        "city": data["city"]["name"],
        "min_temp": min(temps),
        "max_temp": max(temps),
        "max_pop": max(pops) * 100,
        "description": max(set(descriptions), key=descriptions.count),
    }


def build_message(city_name, forecast):
    today_str = datetime.now().strftime("%Y-%m-%d")
    return (
        f"\U0001F324 {today_str} {city_name} 오늘의 날씨 예보\n\n"
        f"날씨: {forecast['description']}\n"
        f"최저 기온: {forecast['min_temp']:.1f}°C\n"
        f"최고 기온: {forecast['max_temp']:.1f}°C\n"
        f"강수 확률: {forecast['max_pop']:.0f}%"
    )


def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    response = requests.post(
        url, data={"chat_id": TELEGRAM_CHAT_ID, "text": text}, timeout=10
    )
    response.raise_for_status()


def send_daily_weather():
    try:
        lat, lon, location_name = get_current_location()
        forecast = get_today_forecast(lat, lon)
        message = build_message(forecast["city"] or location_name, forecast)
        send_telegram_message(message)
        print(f"[{datetime.now()}] 날씨 알림 전송 완료")
    except Exception as e:
        print(f"[{datetime.now()}] 날씨 알림 전송 실패: {e}")


def main():
    missing = [
        name
        for name, val in [
            ("TELEGRAM_BOT_TOKEN", TELEGRAM_BOT_TOKEN),
            ("TELEGRAM_CHAT_ID", TELEGRAM_CHAT_ID),
            ("OPENWEATHER_API_KEY", OPENWEATHER_API_KEY),
        ]
        if not val
    ]
    if missing:
        print(f"환경변수가 설정되지 않았습니다: {', '.join(missing)}")
        sys.exit(1)

    if "--now" in sys.argv:
        send_daily_weather()
        return

    schedule.every().day.at("06:00").do(send_daily_weather)
    print("스케줄러 시작: 매일 06:00에 날씨 예보를 전송합니다.")
    while True:
        schedule.run_pending()
        time.sleep(30)


if __name__ == "__main__":
    main()
