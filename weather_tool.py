import requests

def get_taipei_current_temperature() -> dict:
    """
    取得台北市中心即時溫度。
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 25.0478,
        "longitude": 121.5319,
        "current": "temperature_2m",
        "timezone": "Asia/Taipei",
    }
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()

    return {
        "location": "台北市中心",
        "temperature": data["current"]["temperature_2m"],
        "unit": data["current_units"]["temperature_2m"],
        "time": data["current"]["time"],
    }

# output = get_taipei_current_temperature()
# print(output)