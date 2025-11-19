import pandas as pd
import random

# Configuração dos dados simulados
qtd_registros = 1000
dados = []

trilhas = ['Desenvolvimento Full Stack', 'Data Science', 'Marketing Digital', 'Design UX/UI']
niveis_interesse = [1, 2, 3, 4, 5] # 1 (Baixo) a 5 (Alto)

for _ in range(qtd_registros):
    idade = random.randint(18, 55)
    tempo_desemprego_meses = random.randint(0, 24)
    renda_familiar = random.randint(1500, 15000)
    
    # Simula respostas de um questionário (0 = Não, 1 = Sim)
    gosta_matematica = random.choice([0, 1])
    gosta_arte = random.choice([0, 1])
    gosta_comunicacao = random.choice([0, 1])
    interesse_tecnologia = random.choice(niveis_interesse)
    
    # Lógica simples para definir a trilha (para a IA conseguir aprender padrões)
    if gosta_matematica and interesse_tecnologia > 3:
        trilha = 'Data Science'
    elif gosta_arte and interesse_tecnologia > 2:
        trilha = 'Design UX/UI'
    elif gosta_comunicacao:
        trilha = 'Marketing Digital'
    else:
        trilha = 'Desenvolvimento Full Stack'
        
    dados.append([idade, tempo_desemprego_meses, renda_familiar, gosta_matematica, gosta_arte, gosta_comunicacao, interesse_tecnologia, trilha])

# Criar DataFrame e salvar
df = pd.DataFrame(dados, columns=['idade', 'tempo_desemprego', 'renda_familiar', 'matematica', 'arte', 'comunicacao', 'nivel_tec', 'trilha_recomendada'])
df.to_csv('dados_recomece.csv', index=False)
print("Arquivo 'dados_recomece.csv' gerado com sucesso!")