import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Carregar os dados
df = pd.read_csv('dados/desafio_indicium_imdb-v2.csv')

# Verificar colunas disponíveis
print("Colunas disponíveis no CSV:")
print(df.columns.tolist())

# Limpar a coluna 'Gross': remover pontos, trocar vírgula por ponto e converter para float
df['Gross'] = df['Gross'].astype(str).str.replace('.', '', regex=False)
df['Gross'] = df['Gross'].str.replace(',', '.', regex=False)
df['Gross'] = pd.to_numeric(df['Gross'], errors='coerce')

# Remover linhas com valores ausentes
df = df.dropna(subset=['Gross', 'No_of_Votes', 'Meta_score'])

# Selecionar variáveis
X = df[['Gross', 'No_of_Votes']]
y = df['Meta_score']

# Treinar modelo
model = LinearRegression()
model.fit(X, y)

# Salvar modelo
with open('models/imdb_rating_predictor.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Modelo treinado e salvo com sucesso!")

