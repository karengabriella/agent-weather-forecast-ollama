from llm.ollama_client import extract_weather_params
from tools.forecast import get_daily_forecast
from tools.geocode import geocode_city
from services.format_weather import format_weather, format_weather_response
from log.log_config import setup_logger

logger = setup_logger()


def handle_user_message(user_message: str):
    logger.info("Nova mensagem recebida: %s", user_message)

    try:
        params = extract_weather_params(user_message)
        logger.info("Parâmetros extraídos: %s", params)
    except Exception as e:
        logger.exception("Erro ao extrair parâmetros da mensagem: %s", e)
        return "Não consegui entender sua pergunta no momento. Tente reformular."

    if params["intent"] == "out_of_scope":
        logger.warning("Mensagem fora do escopo.")
        return "Desculpe, sou um assistente meteorológico, pode contar comigo para perguntas sobre o clima."

    if params["city"] is None and params["lat"] is None and params["lon"] is None:
        logger.warning("Localização ausente.")
        return "Preciso da cidade ou das coordenadas para fazer essa consulta."

    if params["city"] is None and (params["lat"] is None or params["lon"] is None):
        logger.warning("Coordenadas incompletas.")
        return "Preciso da cidade ou das coordenadas completas para fazer essa consulta."

    try:
        if params["city"]:
            logger.info("Executando geocode para cidade: %s", params["city"])
            lat, lon, city = geocode_city(params["city"])
            logger.info("Geocode resolvido: city=%s lat=%s lon=%s", city, lat, lon)
        else:
            lat = params["lat"]
            lon = params["lon"]
            city = "coordenadas informadas"
            logger.info("Usando coordenadas fornecidas: lat=%s lon=%s", lat, lon)

    except ValueError as e:
        logger.warning("Erro de validação no geocode: %s", e)
        return "Não consegui encontrar essa localização. Verifique o nome da cidade ou as coordenadas."
    except Exception as e:
        logger.exception("Erro ao resolver localização: %s", e)
        return "Não consegui consultar a localização no momento. Tente novamente em instantes."

    try:
        logger.info("Consultando forecast para %s dias.", params["days"])
        forecast = get_daily_forecast(lat, lon, params["days"])
        logger.info("Forecast obtido com sucesso. Total de dias retornados: %s", len(forecast))

    except Exception as e:
        logger.exception("Erro ao consultar forecast: %s", e)
        return "Não consegui consultar a previsão do tempo no momento. Tente novamente em instantes."

    try:

        if params["target_day"] == "tomorrow":

            if len(forecast) < 2:
                logger.warning("Forecast insuficiente para tomorrow.")
                return "Não consegui obter a previsão para amanhã no momento."

            day = forecast[1]

            logger.info(
                "Forecast selecionado | city=%s date=%s precipitation=%s",
                city,
                day["date"],
                day["precipitation"]
            )

            response = format_weather(day, params["weather_focus"], city)

        elif params["target_day"] == "range":

            if not forecast:
                logger.warning("Forecast vazio para range.")
                return "Não consegui obter a previsão para o período solicitado."

            for day in forecast[:params["days"]]:
                logger.info(
                    "Forecast range | city=%s date=%s precipitation=%s",
                    city,
                    day["date"],
                    day["precipitation"]
                )

            response = format_weather_response(
                forecast[:params["days"]],
                params["weather_focus"],
                city,
                date_range=True
            )

        else:

            if not forecast:
                logger.warning("Forecast vazio para today.")
                return "Não consegui obter a previsão no momento."

            day = forecast[0]

            logger.info(
                "Forecast selecionado | city=%s date=%s precipitation=%s",
                city,
                day["date"],
                day["precipitation"]
            )

            response = format_weather(day, params["weather_focus"], city)

        logger.info("Resposta final gerada com sucesso.")
        return response

    except Exception as e:
        logger.exception("Erro ao formatar resposta: %s", e)
        return "Consegui consultar os dados, mas houve um erro ao montar a resposta."