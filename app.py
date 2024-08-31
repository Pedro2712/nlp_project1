from flask import Flask, request, jsonify, render_template_string
import markdown

app = Flask(__name__)

# Basic CSS to style the markdown content
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

@app.route("/")
def explanation():
    with open("README.md", "r") as file:
        content = file.read()
    
    # Convert markdown to HTML
    html_content = markdown.markdown(content)
    
    # Wrap the HTML content with a simple template that includes the CSS
    full_html = f"""
    <html>
    <head>
        <title>README</title>
        <style>{css}</style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    return render_template_string(full_html)

# Mock function to simulate document retrieval
def search_documents(query):
    # This is a mock implementation.
    # Replace this with your actual search logic.
    documents = [
        {'title': 'Document 1', 'content': 'Content of document 1', 'relevance': 0.9},
        {'title': 'Document 2', 'content': 'Content of document 2', 'relevance': 0.8},
        # Add more documents here
    ]
    # Sort documents by relevance (descending)
    sorted_documents = sorted(documents, key=lambda x: x['relevance'], reverse=True)
    # Return up to 10 documents
    return sorted_documents[:10]

@app.route('/query', methods=['GET'])
def query():
    query_param = request.args.get('query')
    
    if not query_param:
        return jsonify({'message': 'No query parameter provided'}), 400
    
    results = search_documents(query_param)
    
    return jsonify({'results': results, 'message': 'OK'})

if __name__ == '__main__':
    app.run(host='10.103.0.28', port=2712)
