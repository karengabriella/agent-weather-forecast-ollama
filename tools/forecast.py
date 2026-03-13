
import requests
from config import OPEN_METEO_BASE_URL 



def fetch_weather_data(lat, lon, days_ahead):

    url = OPEN_METEO_BASE_URL

    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": [ 
            "temperature_2m_max", 
            "temperature_2m_min", 
            "precipitation_sum" ],
        "timezone": "auto",
        "forecast_days": days_ahead
    }

    response = requests.get(url, params=params)
    response = response.json()


    return response


def format_forecast(daily):

    time = daily["daily"]["time"]
    max_temps = daily["daily"]["temperature_2m_max"]
    min_temps = daily["daily"]["temperature_2m_min"]
    rain = daily["daily"]["precipitation_sum"]


    forecast = []

    for date, max_t, min_t, r in zip(time, max_temps, min_temps, rain):
       
       day_forecast = {
            "date": date,
            "temp_max": max_t,
            "temp_min": min_t,
            "precipitation": r
        }
       
       forecast.append(day_forecast)
       
    return forecast



def get_daily_forecast(lat, lon, days):

 return format_forecast(fetch_weather_data(lat, lon, days))



if __name__ == "__main__":
    print(len(get_daily_forecast(-23.55, -46.63, 2)))


