
# 🎬 Desafio Cientista de Dados – Indicium / PProductions (IMDB)

Este projeto tem como objetivo analisar dados de filmes e desenvolver um modelo preditivo para estimar a nota do IMDB, conforme o desafio proposto pela Indicium.
---

## 📂 Estrutura do projeto

```
LH_CD_ElaineDeJesusFonsecaMatos/
│
├── data/                  
│   ├── desafio_indicium_imdb.csv   # Base original (não utilizada diretamente)
│   └── desafio_indicium_imdb-v2.csv # Base tratada
|
├── reports/              
│   ├── eda_imdb.pdf     # Análise exploratória dos dados
│
├── models/             
│   ├── imdb_rating_predictor.pkl   # Modelo treinado (.pkl)
│
├── src/              
│   ├── eda.py
|   ├── model.py
│   └── predict.py
│
├── README.md              # Explicação do projeto em Markdown
└── requirements.txt       # Pacotes utilizados
```

>>>>>>> 2ef5db3 (Subindo o trabalho)

---

## 🎯 Objetivo do Projeto

Explorar os dados de filmes para gerar insights relevantes e desenvolver um modelo preditivo que auxilie na tomada de decisão sobre futuros lançamentos cinematográficos.

---

## ⚙️ Como Executar

1. Instale os pacotes necessários:
```bash
pip install -r requirements.txt
```
2. Treine o modelo:
```bash
python src/model.py
```
3. Faça uma previsão com o modelo treinado:
```bash
python src/predict.py
```

🧠 Respostas ao Desafio

1. Qual filme você recomendaria para uma pessoa que você não conhece? 
- Como não conhecemos o usuário, eu recomendaria filmes com as melhores notas.

2. Quais fatores estão relacionados com alta expectativa de faturamento?
- Número de votos
- Gêneros populares
- Presença de atores renomados
- Diretores reconhecidos

3. Insights da coluna Overview: 
- Palavras-chave podem indicar o gênero. Ex: “battle”, “hero”, “space” sugerem Action/Sci-Fi.

4. Como prever a nota do IMDB?
- Tipo de problema: Regressão
- Variáveis: Meta_score, No_of_Votes, Gross

5. Previsão para o filme exemplo: 
-Com base nos dados disponíveis, o modelo estima um Meta_score próximo de 80, o que se alinha com a reputação do filme The Shawshank Redemption.

🛠️ Ferramentas e Tecnologias
- Python
- Pandas e NumPy (manipulação de dados)
- Scikit-learn (modelagem preditiva)
- Matplotlib e Seaborn (visualizações, se aplicável)

📬 Entrega
Este projeto foi desenvolvido como parte do processo seletivo da Indicium. O repositório foi nomeado como LH_CD_ElaineDeJesusFonsecaMatos conforme solicitado.
