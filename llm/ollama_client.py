import requests
import json
from config import OLLAMA_BASE_URL, OLLAMA_MODEL

schema = {
    "type": "object",
    "properties": {
        "intent": {"type": "string"},
        "city": {"type": ["string", "null"]},
        "lat": {"type": ["number", "null"]},
        "lon": {"type": ["number", "null"]},
        "days": {"type": ["integer", "null"]},
        "target_day": {"type": ["string", "null"]},
        "weather_focus": {"type": "string"}
    },
    "required": ["intent", "city", "lat", "lon", "days", "target_day"]
}

def extract_weather_params(user_message: str) -> dict:

    response = requests.post(
        OLLAMA_BASE_URL,
        json={
            "model": OLLAMA_MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "Você é um extrator de parâmetros para um agente meteorológico. "
                        "Seu papel não é responder à pergunta do usuário. "
                        "Seu papel é apenas extrair informações e retornar somente um JSON válido. "

                        "Regras: "
                        "1. Se a pergunta for sobre clima, chuva, temperatura, previsão do tempo ou condições meteorológicas, use intent='weather_request'. "
                        "2. Se não for sobre meteorologia, use intent='out_of_scope'. "
                        "3. Se o usuário informar uma cidade, preencha city com o nome da cidade. "
                        "4. Se o usuário informar latitude e longitude, preencha lat e lon com valores numéricos e city deve ser null. "
                        "5. Se o usuário não informar quantidade de dias, use days=1. "
                        "6. Se o usuário disser 'hoje', use target_day='today' e days=1. "
                        "7. Se o usuário disser 'amanhã', use target_day='tomorrow' e days=2. "
                        "8. Se o usuário pedir vários dias, use target_day='range'. "
                        "9. Se o usuário não informar localização, city, lat e lon devem ser null. "
                        "10. Nunca use textos como 'Not specified'. Use apenas null quando a informação não existir. "
                        "11. Retorne somente JSON válido, sem explicações, sem comentários e sem markdown."
                        "12. Não invente dados além das regras estabelicidas para substituição, seu papel não conseder dados metereológicos. "
                        "13. Seu papel é abstrair o conteúdo e contexto da conversa de acordo com as regras estabelicidas"
                        "15. Defina o weather_focus se é chuva, temperatura ou geral com base no contexto da pergunta"
                        
                       "15. Use sempre esta estrutura de json: "
                        "{"
                        "intent: string, "
                        "city: string ou null, "
                        "lat: number ou null, "
                        "lon: number ou null, "
                        "days: integer ou null, "
                        "target_day: string ou null"
                        "weather_focus: rain or temperature or general"
                        "}. "
                          
                    )
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            "format": schema,
            "stream": False
        }
    )

    response = response.json()
    content = response["message"]["content"].strip()

    content_parsed = json.loads(content)

    return content_parsed



if __name__ == "__main__":
    
    print(json.dumps(extract_weather_params("Vai chover hoje?"), indent=4, ensure_ascii=False))