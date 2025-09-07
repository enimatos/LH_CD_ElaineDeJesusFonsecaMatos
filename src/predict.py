import pickle
import pandas as pd

# Carregar o modelo salvo
with open('models/imdb_rating_predictor.pkl', 'rb') as f:
    model = pickle.load(f)

# Dados do filme exemplo (valores numéricos)
filme_exemplo = {
    'Gross': 28341469.00,         # Valor convertido para float
    'No_of_Votes': 2343110        # Número de votos
}

# Transformar em DataFrame
df_filme = pd.DataFrame([filme_exemplo])

# Fazer a previsão
meta_score_previsto = model.predict(df_filme)[0]
print(f'Meta Score previsto: {round(meta_score_previsto, 2)}')

