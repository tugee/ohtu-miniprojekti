from app import app
from db import db
from flask import render_template

@app.route("/")
def index():
    result = db.session.execute("SELECT tunnus FROM kayttajat")
    ekarivi = result.fetchone()
    testi = ekarivi.tunnus
    return render_template("index.html", testi=testi)
