# API de Busca de Filmes

### Visão Geral
Este projeto fornece uma API baseada em Flask para buscar descrições de filmes com base em uma consulta. A API utiliza a vetorização TF-IDF e a similaridade cosseno para classificar e recuperar os filmes mais relevantes de um dataset, com base em uma consulta fornecida pelo usuário.

### Instalação
Para começar, você precisará instalar as dependências necessárias. Este projeto utiliza Python 3 e as seguintes bibliotecas:

1. Clone o repositório:

```bash
git clone <url-do-seu-repositorio>
cd <diretorio-do-seu-repositorio>
```
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Baixe o dataset:

- Coloque o arquivo do dataset (Movies_Reviews_modified_version1.csv) no diretório raiz do projeto.
Como Executar
Depois de instalar as dependências, você pode executar o servidor Flask:

### Como Executar

```bash
python app.py
```
O servidor será iniciado em http://localhost:2712.

### Como Funciona
#### Funcionalidade Principal

A API utiliza a vetorização TF-IDF (Term Frequency-Inverse Document Frequency) para converter as descrições dos filmes em vetores, que são então comparados usando similaridade cosseno para classificar a relevância de cada filme em relação à consulta do usuário.

#### Endpoints

- `/query?query=<sua-consulta>`: Este endpoint aceita uma solicitação GET com um parâmetro de consulta e retorna um objeto JSON contendo os filmes mais relevantes.
  

Exemplo:

```bash
curl "http://localhost:2712/query?query=filme+de+super-herói+com+elementos+de+comédia"
```

### Fonte de Dados
O dataset utilizado neste projeto é chamado Movies_Reviews_modified_version1.csv. Ele contém títulos de filmes, avaliações, gêneros, descrições e emoções relacionadas aos filmes. Este dataset foi processado para incluir tanto resenhas de usuários quanto descrições de filmes, proporcionando uma rica fonte de informações para buscas baseadas em consultas.

### Testes

#### Casos de Teste

Aqui estão alguns casos de teste com links diretos que você pode usar para testar a API:

1. Um Teste Que Retorna 10 Resultados

- Consulta: `"action-packed adventure"`
- Comentário: Buscar por `"action-packed adventure"` retorna 10 filmes relevantes que se enquadram nos gêneros de ação e aventura.

1. Um Teste Que Retorna Mais de 1, mas Menos de 10 Resultados

- Consulta: `"romantic musical set in the 1980s"`
- Comentário: Buscar por `"romantic musical set in the 1980s"` retorna um conjunto específico de filmes, provavelmente entre 2 e 9, pois é uma consulta mais nichada.

1. Um Teste Que Retorna Algo Não Óbvio

- Consulta: `"cyberpunk detective noir"`
- Comentário: Esta consulta pode retornar um resultado não óbvio, como um thriller de ficção científica que se encaixa no clima de `"cyberpunk detective noir"`, mesmo que essas palavras exatas não estejam na descrição do enredo. A relevância vem dos elementos temáticos, em vez de correspondências diretas de palavras-chave.