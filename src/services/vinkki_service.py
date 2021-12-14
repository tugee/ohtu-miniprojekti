from repositories.vinkki_repository import (
    vinkki_repository as default_vinkki_repository
)

class VinkkiService:
    def __init__(self, vinkki_repository=default_vinkki_repository):
        self._vinkki_repository = vinkki_repository

    def search_vinkkis(self):
        list = self._vinkki_repository.find_by_vinkki()
        return list
    
    def search_own_vinkkis(self, tekija):
        list = self._vinkki_repository.find_by_user(tekija)
        return list

    def create_vinkki(self, nimi, url, tekija):
        self._vinkki_repository.create(nimi, url, tekija)

    def delete_vinkki(self, nimi):
        self._vinkki_repository.delete(nimi)

    def hide_vinkki(self, nimi):
        self._vinkki_repository.hide(nimi)

    def set_read_vinkki(self, id):
        self._vinkki_repository.set_read(id)
        self._vinkki_repository.set_read_date(id)

    def set_unread_vinkki(self, id):
        self._vinkki_repository.set_unread(id)

vinkki_service = VinkkiService()
