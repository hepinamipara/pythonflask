from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data with image_url
books = [
    {
        "id": 1,
        "title": "Flask for Beginners",
        "author": "Alice",
        "image_url": "https://imgs.search.brave.com/K6CpDI9b7Q0ACZR5foIdxE6AZVtEUfCaRCZMBj9AslM/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/cGl4YWJheS5jb20v/cGhvdG8vMjAyMS8w/MS8yMS8xNS81NC9i/b29rcy01OTM3NzE2/XzY0MC5qcGc"
    },
    {
        "id": 2,
        "title": "Advanced Python",
        "author": "Bob",
        "image_url": "https://imgs.search.brave.com/rHjdKrt7C_XVLFPhpjMWx2WyOucBADyJMmJVukw_QUk/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pbWFn/ZXMucGV4ZWxzLmNv/bS9waG90b3MvMTU5/ODY2L2Jvb2tzLWJv/b2stcGFnZXMtcmVh/ZC1saXRlcmF0dXJl/LTE1OTg2Ni5qcGVn/P2F1dG89Y29tcHJl/c3MmY3M9dGlueXNy/Z2ImZHByPTEmdz01/MDA"
    }
]

# Home route
@app.route('/')
def home():
    return "Welcome to the Book API!"

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Get a single book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

# Add a new book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    new_book["id"] = len(books) + 1
    new_book["image_url"] = new_book.get("image_url", "")
    books.append(new_book)
    return jsonify(new_book), 201

# Run the app on default port 5000
if __name__ == '__main__':
    app.run(debug=True)
