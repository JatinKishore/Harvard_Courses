from flask import Flask, render_template, request, redirect
from cs50 import SQL

app = Flask(__name__)

db = SQL("sqlite:///forshims.db")

SPORTS = ["Basketball","Soccer","Ultimate Frishbee"]

REGISTERS = {}
@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods = ["POST"])
def register():
    NAME = request.form.get("name")
    if not request.form.get("name"):   
        msg = "Plz enter a Valid Name"      
        return render_template("error.html",message = msg)      
    
    if not request.form.getlist("sport"):
        msg  = "You haven't chosen any sports name , Please choose atleast one sports name"
        return render_template("error.html", message = msg)  
    SPORT = request.form.get("sport")
    db.execute("INSERT INTO registerants (name,sport) VALUES(?,?)", NAME, SPORT)
    return redirect("/registerants")

@app.route("/registerants")
def registerants():
    RESGISTERANTS = db.execute("SELECT * FROM registerants")
    return render_template("register.html",registerants = RESGISTERANTS)

@app.route("/deregister", methods = ["POST"])
def deregisterants():
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM registerants WHERE id=?",id)
    return redirect("/registerants")



