from flask.wrappers import Request
from app import app
from db import db
from flask import render_template, redirect, session, request
from werkzeug.security import check_password_hash, generate_password_hash

@app.route("/")
def index():
    result = db.session.execute("SELECT tunnus FROM kayttajat")
    ekarivi = result.fetchone()
    testi = ekarivi.tunnus
    return render_template("index.html", testi=testi)

@app.route("/donewuser", methods=["POST"])
def donewuser():
    username = request.form["username"]
    password = request.form["password"]
    sql = "INSERT INTO kayttajat (tunnus,salasana) VALUES (:username,:password)"
    hash_value = generate_password_hash(password)
    db.session.execute(sql, {"tunnus": username, "salasana": hash_value})
    db.session.commit()
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
    komento = "SELECT tunnus, salasana FROM kayttajat WHERE tunnus=:tunnus"
    hakutulos = db.session.execute(komento, {"tunnus":username})
    kayttaja = hakutulos.fetchone()
    if not kayttaja:
        return redirect("/kirjautuminen")
    else:
        if password != kayttaja.salasana:
            return redirect("/kirjautuminen")
    session["username"] = username
    return redirect("/kirjautuminen")

@app.route("/logout")   
def logout():
    del session["username"]
    return redirect("/kirjautuminen")