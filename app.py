# Arquivo: app.py
from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Carregar o modelo treinado
try:
    modelo_trilha = joblib.load('modelo_trilha.joblib')
    print("Modelo carregado com sucesso!")
except:
    print("Erro: Rode o notebook de classificação primeiro para gerar o arquivo .joblib")

@app.route('/')
def home():
    return "API ReComece Online! Use o endpoint /recomendar (POST)."

@app.route('/recomendar', methods=['POST'])
def recomendar():
    # 1. Receber os dados do JSON
    dados = request.json
    
    # Exemplo de entrada esperada: 
    # { "matematica": 1, "arte": 0, "comunicacao": 0, "nivel_tec": 5 }
    
    # 2. Transformar em DataFrame (igual ao treinamento)
    df_entrada = pd.DataFrame([dados])
    
    # 3. Fazer a previsão
    predicao = modelo_trilha.predict(df_entrada)[0]
    
    # 4. Retornar resposta
    return jsonify({
        "perfil_analisado": dados,
        "trilha_recomendada": predicao,
        "mensagem": "Recomendação gerada via IA ReComece."
    })

if __name__ == '__main__':
    app.run(debug=True)