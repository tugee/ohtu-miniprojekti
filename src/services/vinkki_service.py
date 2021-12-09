from repositories.vinkki_repository import (
    vinkki_repository as default_vinkki_repository
)

class VinkkiService:
    def __init__(self, vinkki_repository=default_vinkki_repository):
        self._vinkki_repository = vinkki_repository

    def search_vinkkis(self):
        list = self._vinkki_repository.find_by_vinkki()
        return list

    def create_vinkki(self, nimi, url, tekija):
        self._vinkki_repository.create(nimi, url, tekija)

    def delete_vinkki(self, id):
        self._vinkki_repository.delete(id)
    
    def hide_vinkki(self, id):
        self._vinkki_repository.hide(id)

vinkki_service = VinkkiService()
