from flask.wrappers import Request
from app import app
from db import db
from flask import render_template, redirect, session, request

@app.route("/")
def index():
    result = db.session.execute("SELECT tunnus FROM kayttajat")
    ekarivi = result.fetchone()
    testi = ekarivi.tunnus
    return render_template("index.html", testi=testi)

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
        if password != kayttaja.password:
            return redirect("/kirjautuminen")
    session["username"] = username
    return redirect("/kirjautuminen")

@app.route("/logout")   
def logout():
    del session["username"]
    return redirect("/kirjautuminen")