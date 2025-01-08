from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

LIBRARY_1_URL = 'http://example.com/library1'
LIBRARY_2_URL = 'http://example.com/library2'

@app.route('/clone', methods=['POST'])
def clone_library():
    try:
        # Fetch data from library 1
        response = requests.get(LIBRARY_1_URL)
        response.raise_for_status()
        library1_data = response.json()

        # Post data to library 2
        response = requests.post(LIBRARY_2_URL, json=library1_data)
        response.raise_for_status()

        return jsonify({"message": "Library cloned successfully!"}), 200

    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/books', methods=['GET'])
def get_books():
    try:
        # Fetch books from the library
        response = requests.get(LIBRARY_1_URL)
        response.raise_for_status()
        books = response.json()
        return render_template('books.html', books=books)

    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/search', methods=['GET'])
def search_books():
    query = request.args.get('q', '')
    try:
        # Fetch books from the library
        response = requests.get(LIBRARY_1_URL)
        response.raise_for_status()
        books = response.json()
        # Filter books based on the search query
        filtered_books = [book for book in books if query.lower() in book['title'].lower()]
        return render_template('books.html', books=filtered_books)

    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
