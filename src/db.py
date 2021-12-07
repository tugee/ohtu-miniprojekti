from os import getenv
from flask_sqlalchemy import SQLAlchemy
from app import app

uri = getenv("DATABASE_URL")
app.secret_key = getenv("SECRET_KEY")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config["SQLALCHEMY_DATABASE_URI"] = uri
db = SQLAlchemy(app)
