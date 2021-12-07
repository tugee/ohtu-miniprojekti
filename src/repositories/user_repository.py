from db import db
from sqlalchemy import text

class UserRepository:
    def __init__(self):
        pass

    def find_by_username(self, username):
        sql = text("SELECT tunnus, salasana FROM kayttajat WHERE tunnus=:tunnus")
        result = db.session.execute(sql, {"tunnus": username})
        return result.fetchone()
    
    def create(self, username, password_hash):
        sql = text("INSERT INTO kayttajat (tunnus, salasana) VALUES (:username, :password)")
        db.session.execute(sql, {"username":username, "password":password_hash})
        db.session.commit()

user_repository = UserRepository()
