from flask import Flask, render_template, request, jsonify
from cs50 import SQL

# Configure app
app = Flask(__name__)

# Connect to database
db = SQL("sqlite:///store.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    q = request.args.get("q")
    if q:
        books = db.execute("SELECT * FROM books WHERE title LIKE ?", "%" + q + "%")
    else:
        books = []
    return jsonify(books)
