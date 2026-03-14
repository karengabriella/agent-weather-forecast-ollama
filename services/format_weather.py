from services.weather_rules import rain_description, will_rain
from datetime import datetime


def format_weather(day: dict, weather_focus, date_range=None) -> str:
    rain_mm = day["precipitation"]
    rain_text = rain_description(rain_mm)
    raining = will_rain(rain_mm)

    if date_range:
        formatted_date = format_dates(day["date"])
    else:
        formatted_date = format_date(day["date"])

    if weather_focus == "rain" and raining:
        return (
            f"📅 {formatted_date}\n"
            f"🌧️ {rain_text} ({rain_mm} mm).\n"
            f"🌡️ Temperatura entre {day['temp_min']}°C e {day['temp_max']}°C."
        )

    elif weather_focus == "temperature":
        return (
            f"📅 {formatted_date}\n"
            f"🌡️ Temperaturas entre {day['temp_min']}°C e {day['temp_max']}°C"
        )

    else:
        return (
            f"📅 {formatted_date}\n"
            f"🌡️ {day['temp_min']}°C — {day['temp_max']}°C\n"
            f"🌧️ {rain_text}"
        )


def format_weather_response(days: list[dict], weather_focus, city, date_range=None) -> str:
    formatted_days = [
        format_weather(day, weather_focus, date_range=date_range)
        for day in days
    ]

    return f"📍 Resultados para {city}\n\n" + "\n\n".join(formatted_days)


def format_dates(date_str: str) -> str:
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    day = date_obj.day
    month = months[date_obj.month - 1]
    return f"{day} de {month}"


def format_date(date_str: str) -> str:
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    weekday = weekdays[date_obj.weekday()]
    day = date_obj.day
    month = months[date_obj.month - 1]
    return f"{weekday}, {day} de {month}"


def format_location(place: dict) -> str:

    city = place.get("name")
    try:
     state_name = place.get("admin1")
    except:
        state_name = ''


    state_abbr = STATE_ABBR.get(state_name, state_name)

    return f"{city}, {state_abbr}"


weekdays = [
    "segunda","terça","quarta","quinta","sexta","sábado","domingo"
]

months = [
    "janeiro","fevereiro","março","abril","maio","junho",
    "julho","agosto","setembro","outubro","novembro","dezembro"
]

STATE_ABBR = {
    "Acre": "AC",
    "Alagoas": "AL",
    "Amapá": "AP",
    "Amazonas": "AM",
    "Bahia": "BA",
    "Ceará": "CE",
    "Distrito Federal": "DF",
    "Espírito Santo": "ES",
    "Goiás": "GO",
    "Maranhão": "MA",
    "Mato Grosso": "MT",
    "Mato Grosso do Sul": "MS",
    "Minas Gerais": "MG",
    "Pará": "PA",
    "Paraíba": "PB",
    "Paraná": "PR",
    "Pernambuco": "PE",
    "Piauí": "PI",
    "Rio de Janeiro": "RJ",
    "Rio Grande do Norte": "RN",
    "Rio Grande do Sul": "RS",
    "Rondônia": "RO",
    "Roraima": "RR",
    "Santa Catarina": "SC",
    "São Paulo": "SP",
    "Sergipe": "SE",
    "Tocantins": "TO"
}
