# agent-weather-forecast-ollama

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Ollama](https://img.shields.io/badge/LLM-Ollama-green)
![API](https://img.shields.io/badge/API-Open--Meteo-orange)

**PT** | Agente simples de IA usando Ollama com tool/function calling para obter previsão do tempo via Open-Meteo.<br>
**EN** | Simple AI agent using Ollama with tool/function calling to retrieve weather forecasts from the Open-Meteo API.

---

# 📌 Sobre o projeto | About the Project

**PT**

Este projeto implementa um agente de IA capaz de responder perguntas meteorológicas utilizando um modelo LLM local via **Ollama** e integrando com a API **Open-Meteo** para obter previsões do tempo.

O agente interpreta perguntas em linguagem natural, extrai parâmetros relevantes e decide quando chamar ferramentas externas para obter dados meteorológicos.

**EN**

This project implements an AI agent capable of answering weather-related questions using a local LLM via **Ollama** and integrating with the **Open-Meteo** API to retrieve weather forecasts.

The agent interprets natural language questions, extracts relevant parameters and decides when to call external tools to obtain weather data.

---

# 🧠 Arquitetura do agente | Agent Architecture

Fluxo principal do sistema:

```
User message
↓
LLM parameter extraction (Ollama)
↓
Structured JSON
↓
Agent decision logic
↓
Geocoding (city → lat/lon)
↓
Weather forecast (Open-Meteo API)
↓
Formatted response
```

---

# 🗂 Estrutura do projeto | Project Structure

```
weather-agent/
│
├── main.py
├── agent.py
├── config.py
│
├── llm/
│   └── ollama_client.py
│
├── tools/
│   ├── forecast.py
│   └── geocode.py
│
├── services/
│   ├── format_weather.py
│   └── weather_rules.py
│
├── log/
│   └── log_config.py
│
└── README.md
```

---

# ⚙️ Tecnologias utilizadas | Technologies

* Python
* Ollama (LLM local)
* Open-Meteo API
* Open-Meteo Geocoding API
* Requests
* Logging (observability)

---

# 🚀 Como rodar o projeto | How to Run

## 1️⃣ Clonar o repositório

```
git clone https://github.com/seu-usuario/agent-weather-forecast-ollama.git
cd agent-weather-forecast-ollama
```

---

## 2️⃣ Instalar dependências


```
pip install requests
```

---

## 3️⃣ Instalar e rodar Ollama

Instale Ollama:

https://ollama.com/

Depois rode o modelo:

```
ollama run phi3:mini
```

---

## 4️⃣ Executar o agente

```
python main.py
```

---

# 💬 Exemplos de perguntas | Example Questions

```
Vai chover hoje em São Paulo?
Como estará o clima amanhã em Florianópolis?
Qual a previsão para os próximos 3 dias em Curitiba?
Vai fazer frio amanhã em Porto Alegre?
```

---

# 🧩 Funcionalidades

✔ Interpretação de perguntas em linguagem natural
✔ Extração estruturada de parâmetros via LLM
✔ Integração com API meteorológica
✔ Geocoding de cidades
✔ Previsão para múltiplos dias
✔ Tratamento de erros
✔ Logs para observabilidade

---

# 📊 Observabilidade

O agente registra logs de execução contendo:

* mensagem do usuário
* parâmetros extraídos pelo LLM
* resolução de geolocalização
* chamadas à API de previsão
* forecast selecionado (data e precipitação)
* erros de integração

Os logs são armazenados em:

```
/log/weather_agent.log
```

---

# 🔎 Exemplo de log

```
INFO | Nova mensagem recebida: Vai chover amanhã em Florianópolis?
INFO | Parâmetros extraídos: {...}
INFO | Executando geocode para cidade: Florianópolis
INFO | Geocode resolvido: city=Florianópolis lat=-27.59667 lon=-48.54917
INFO | Forecast selecionado | city=Florianópolis date=2026-03-14 precipitation=0.0
```

---

# ⚠️ Tratamento de erros

O agente trata cenários como:

* cidade não encontrada
* coordenadas inválidas
* falha na API
* resposta inesperada
* pergunta fora de escopo

---

# 📈 Possíveis melhorias

* Interface web com **Gradio**
* Memória de conversa
* Suporte a múltiplos idiomas
* Cache de consultas meteorológicas
* Integração com observabilidade avançada

---

# 👩 Autora

Projeto desenvolvido como parte de um desafio técnico para implementação de um agente LLM com tool calling.
