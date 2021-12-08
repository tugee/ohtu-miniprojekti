from flask import (
    render_template, redirect, session, request
)
from app import app
from services.user_service import user_service

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ping")
def ping():
    return "pong"

@app.route("/donewuser", methods=["POST"])
def donewuser():
    username = request.form["username"]
    password = request.form["password"]
    user_service.create_user(username, password)
    return redirect("/kirjautuminen")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/kirjautuminen")
def kirjautuminen():
    return render_template("kirjautuminen.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    kayttaja = user_service.check_credentials(username, password)
    if kayttaja:
        session["username"] = username
    return redirect("/kirjautuminen")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/kirjautuminen")
