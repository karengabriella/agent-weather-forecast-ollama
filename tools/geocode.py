import requests
from services.format_weather import format_location
from config import GEOCODING_BASE_URL, REQUEST_TIMEOUT

def geocode_city(city: str, count: int = 1, language: str = "pt") -> dict | None:
 
    url = GEOCODING_BASE_URL
    params = {
        "name": city,
        "count": count,
        "language": language,
        "format": "json",
    }

    response = requests.get(url, params=params, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()


    data = response.json()
    results = data.get("results")

    if not results:
        return None

    place = results[0]

    return (
  
        place.get("latitude"),
        place.get("longitude"),
        format_location(place)
    )


if __name__ == "__main__":
    lat, lon, city = geocode_city("São Paulo")
    print(lat, lon, city)