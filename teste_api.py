# Arquivo: teste_api.py
import requests
import json

# URL da sua API (verifique se o número da porta é 5000 mesmo no terminal da API)
url = 'http://127.0.0.1:5000/recomendar'

# Dados simulados de um usuário (Front-end enviaria isso)
dados_usuario = {
    "matematica": 1,       # 1 = Gosta, 0 = Não gosta
    "arte": 0,             # 0 = Não gosta
    "comunicacao": 0,      # 0 = Não gosta
    "nivel_tec": 5         # Nível de interesse em tecnologia (1 a 5)
}

# Envia o pedido POST para a API
response = requests.post(url, json=dados_usuario)

# Mostra a resposta da IA
print("Status:", response.status_code)
print("Resposta da IA:", response.json())