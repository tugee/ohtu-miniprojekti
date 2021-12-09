from flask import (
    render_template, redirect, session, request
)
from app import app
from services.user_service import user_service
from services.vinkki_service import vinkki_service

@app.route("/")
def index():
    vinkki_list = vinkki_service.search_vinkkis()
    return render_template("index.html", vinkki_list=vinkki_list)

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
    return redirect("/")

@app.route("/delete/<vinkki_nimi>")
def delete(vinkki_nimi):
    vinkki_service.delete_vinkki(vinkki_nimi)
    return redirect("/")

app.route("/hide/<vinkki_nimi>")
def hide(vinkki_nimi):
    vinkki_service.hide_vinkki(vinkki_nimi)
    return redirect("/")


@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/kirjautuminen")

@app.route("/uusivinkki")
def uusivinkki():
    return render_template("uusivinkki.html")

@app.route("/lisaavinkki", methods=["POST"])
def lisaavinkki():
    nimi = request.form["nimi"]
    url = request.form["url"]
    tekija = session["username"]
    vinkki_service.create_vinkki(nimi, url, tekija)
    return redirect("/")
