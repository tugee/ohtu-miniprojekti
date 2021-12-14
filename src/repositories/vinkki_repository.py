from sqlalchemy import text
from db import db

class VinkkiRepository:
    def __init__(self):
        pass

    def find_by_vinkki(self):
        sqlcmnd = text("SELECT id, nimi, url, tekija, luettu, paivays FROM lukuvinkit")
        result = db.session.execute(sqlcmnd)
        return result.fetchall()

    def create(self, nimi, url, tekija):
        sql = text("""
        INSERT INTO lukuvinkit (nimi, url, tekija, luettu, paivays)
        VALUES (:nimi, :url, :tekija, false, null)
        """)
        db.session.execute(sql, {"nimi":nimi, "url":url, "tekija":tekija})
        db.session.commit()

    def delete(self, nimi):
        sql = text("DELETE FROM lukuvinkit WHERE nimi=:nimi")
        db.session.execute(sql, {"nimi":nimi})
        db.session.commit()
    
    def hide(self, nimi):
        sql = text("UPDATE lukuvinkit piilotettu=true WHERE nimi=:nimi")
        db.session.execute(sql, {"nimi":nimi})
        db.session.commit()
    

vinkki_repository = VinkkiRepository()
