from flask import Flask, render_template, redirect, session, request
from flask_session import Session
from cs50 import SQL

#configure app
app = Flask(__name__)

#connect to database
db = SQL("sqlite:///store.db")

#Configure Session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    BOOKS = db.execute("SELECT * FROM BOOKS")
    return render_template("books.html",books=BOOKS)

@app.route("/cart", methods = ["GET","POST"])
def cart():

    #ensure cart exsits
    if "cart" not in session:
        session["cart"] = []
    
    # POST
    if request.method == "POST":
        book_id = request.form.get("id")
        if book_id:
            session["cart"].append(book_id)
        return redirect("/cart")
    
    #GET
    SELECTED_BOOKS = db.execute("SELECT * FROM BOOKS WHERE id IN (?)", session["cart"])
    return render_template("cart.html",books=SELECTED_BOOKS)