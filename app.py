from flask import Flask, request, jsonify, render_template_string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd
import markdown
import json

app = Flask(__name__)

url = "Movies_Reviews_modified_version2.csv"
df = pd.read_csv(url)

tfidf = TfidfVectorizer(stop_words='english', max_df=0.8, min_df=2)
tfidf_matrix = tfidf.fit_transform(df['Description'])

css = """
    body {
        font-family: Arial, sans-serif;
        max-width: 800px;
        margin: 20px auto;
        padding: 20px;
        line-height: 1.6;
        color: #333;
        background-color: #f4f4f4;
    }
    h1, h2, h3 {
        color: #444;
    }
    pre {
        background-color: #333;
        color: #f8f8f2;
        padding: 10px;
        border-radius: 5px;
        overflow-x: auto;
    }
    code {
        background-color: #f4f4f4;
        padding: 2px 4px;
        border-radius: 3px;
        font-size: 0.9em;
    }
    a {
        color: #007BFF;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
"""

def most_relevant_movies(query, tfidf_matrix, tfidf, df, threshold=0.2):
    query_vector = tfidf.transform([query])
    cosine_similarities = linear_kernel(query_vector, tfidf_matrix).flatten()
    
    relevant_indices = [i for i, score in enumerate(cosine_similarities) if score >= threshold]
    
    if not relevant_indices:
        return []

    sorted_indices = sorted(relevant_indices, key=lambda i: cosine_similarities[i], reverse=True)
    
    top_indices = sorted_indices[:10]
    
    top_movies = df.iloc[top_indices].drop_duplicates(subset='movie_name')
    results = top_movies[['movie_name', 'Ratings', 'genres', 'Description']].to_dict(orient='records')
    
    return results

@app.route("/")
def explanation():
    try:
        with open("README.md", "r", encoding="utf-8") as file:  # Ler o arquivo README.md com codificação UTF-8
            content = file.read()
    except FileNotFoundError:
        content = "# README\n\nO arquivo README não foi encontrado."

    html_content = markdown.markdown(content)

    full_html = f"""
    <html>
    <head>
        <meta charset="UTF-8">  <!-- Define a codificação como UTF-8 para suportar acentuação -->
        <title>README</title>
        <style>{css}</style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    return render_template_string(full_html)

@app.route('/query', methods=['GET'])
def query():
    query_param = request.args.get('query')

    if not query_param:
        return jsonify({'message': 'No query parameter provided'}), 400

    results = most_relevant_movies(query_param, tfidf_matrix, tfidf, df)

    return jsonify({'results': results, 'message': 'OK'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2712)
