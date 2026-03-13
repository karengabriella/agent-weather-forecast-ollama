
from llm.ollama_client import extract_weather_params
from tools.forecast import get_daily_forecast
from tools.geocode import geocode_city
from services.format_weather import format_weather



def handle_user_message(user_message: str):

    params = extract_weather_params(user_message)

    if params["intent"] == "out_of_scope":
        return "Desculpe, sou um assistente meteorológico, pode contar comigo para perguntas sobre o clima."

    if params["city"] is None and params["lat"] is None and params["lon"] is None:
        return "Preciso da cidade ou das coordenadas para fazer essa consulta."
    
    if params["city"] is None and (params["lat"] is None or params["lon"] is None):
        return "Preciso das cordenadas ou das coordenadas para fazer essa consulta."

    if params["city"]:
        lat, lon, city = geocode_city(params["city"])

    else:
        lat = params["lat"]
        lon = params["lon"]

   

    forecast = get_daily_forecast(lat, lon, params["days"])

    if params["target_day"] == "tomorrow":
     if len(forecast) < 2:
        return "Não consegui obter a previsão para amanhã no momento."
     else:
        response = format_weather(forecast[1],params['weather_focus'], city)

    elif params["target_day"] == "range":

        response = "\n".join(format_weather(day,params['weather_focus'], city, True) for day in forecast)

    else:
        response = format_weather(forecast[0],params['weather_focus'], city)


    return response



print(handle_user_message("vai chover em brasilia nos próximos 3 dias?"))