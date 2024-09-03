import pandas as pd

# Supondo que o DataFrame já esteja carregado como `df`
url = "Movies_Reviews_modified_version1.csv"
df = pd.read_csv(url)

# Agrupar por `movie_name` e concatenar as `Reviews`, mantendo as outras colunas
grouped_df = df.groupby('movie_name').agg({
    'Reviews': lambda x: ' '.join(x),
    'Ratings': 'mean',  # Calcula a média das avaliações
    'Resenhas': lambda x: ' '.join(x),  # Concatenar as resenhas em português
    'genres': 'first',  # Mantém o primeiro gênero (ou pode-se usar alguma outra função)
    'Description': 'first',  # Mantém a primeira descrição (ou pode-se concatenar)
    'emotion': 'first'  # Mantém a primeira emoção (ou pode-se concatenar)
}).reset_index()

# Salvar o DataFrame agrupado em um novo arquivo CSV
grouped_df.to_csv('Movies_Reviews_modified_version2.csv', index=False)
