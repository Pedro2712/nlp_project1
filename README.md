# Flask API Query Endpoint

This API provides a `/query` route that returns up to 10 relevant documents based on a search query.

## API Endpoint

- `GET /query?query=<your_query>`

### Sample Test Cases

1. **Test with 10 Results**

   - **URL:** `http://<your_host>:8888/query?query=example_query`
   - **Comment:** This search should yield exactly 10 results because there are enough relevant documents in the database.

2. **Test with 3 Results**

   - **URL:** `http://<your_host>:8888/query?query=unique_term`
   - **Comment:** This search should yield fewer than 10 results because there are not enough relevant documents.

3. **Test with Non-Obvious Result**

   - **URL:** `http://<your_host>:8888/query?query=ambiguous_term`
   - **Comment:** This search yields non-obvious results because the term is ambiguous, showing documents with different contexts.

### Notes
- Replace `<your_host>` with the actual IP address or domain where your Flask app is hosted.
- The `query` parameter in each test URL should be replaced with terms relevant to your document set.
