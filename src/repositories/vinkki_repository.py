from sqlalchemy import text
from db import db

class VinkkiRepository:
    def __init__(self):
        pass

    def find_by_vinkki(self):
        sql = text("SELECT id, nimi, url, tekija FROM lukuvinkit WHERE piilotettu=FALSE")
        result = db.session.execute(sql)
        return result.fetchall()

    def find_by_user(self, tekija):
        sql = text("""
          SELECT id, nimi, url, luettu, paivays FROM lukuvinkit
          WHERE piilotettu=FALSE AND tekija=:tekija
        """)
        result = db.session.execute(sql, {"tekija":tekija})
        return result.fetchall()

    def create(self, nimi, url, tekija):
        sql = text("""
          INSERT INTO lukuvinkit (nimi, url, tekija, luettu, paivays, piilotettu)
          VALUES (:nimi, :url, :tekija, FALSE, null, FALSE)
        """)
        db.session.execute(sql, {"nimi":nimi, "url":url, "tekija":tekija})
        db.session.commit()

    def hide(self, vinkki_id):
        sql = text("UPDATE lukuvinkit piilotettu=true WHERE id=:id")
        db.session.execute(sql, {"id":vinkki_id})
        db.session.commit()

    def set_read(self, vinkki_id):
        sql = text("UPDATE lukuvinkit SET luettu=true WHERE id=:id")
        db.session.execute(sql, {"id":vinkki_id})
        db.session.commit()

    def set_read_date(self, vinkki_id):
        sql = text("UPDATE lukuvinkit SET paivays=NOW() WHERE id=:id")
        db.session.execute(sql, {"id":vinkki_id})
        db.session.commit()

    def set_unread(self, vinkki_id):
        sql = text("UPDATE lukuvinkit SET luettu=false WHERE id=:id")
        db.session.execute(sql, {"id":vinkki_id})
        db.session.commit()

vinkki_repository = VinkkiRepository()
