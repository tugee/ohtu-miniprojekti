from sqlalchemy import text
from db import db

class VinkkiRepository:
    def __init__(self):
        pass

    def find_by_vinkki(self):
        sqlcmnd = text("SELECT nimi, url, tekija FROM lukuvinkit")
        result = db.session.execute(sqlcmnd)
        return result.fetchall()

    def create(self, nimi, url, tekija):
        sql = text("INSERT INTO lukuvinkit (nimi, url, tekija) VALUES (:nimi, :url, :tekija)")
        db.session.execute(sql, {"nimi":nimi, "url":url, "tekija":tekija})
        db.session.commit()

    def delete(self, id):
        sql = text("DELETE FROM lukuvinkit where id="(id))
        db.session.execute(sql, id)
        db.session.commit()
    
    def hide(self, id):
        sql = text("UPDATE lukuvinkit piilotettu=true where id="(id))
        db.session.execute(sql, id)
        db.session.commit()
    

vinkki_repository = VinkkiRepository()