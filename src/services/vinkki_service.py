from repositories.vinkki_repository import (
    vinkki_repository as default_vinkki_repository
)

class VinkkiService:
    def __init__(self, vinkki_repository=default_vinkki_repository):
        self._vinkki_repository = vinkki_repository

    def search_vinkkis(self):
        pass
        #Tähän vinkkien hakeminen

    def create_vinkki(self, nimi, url, tekija):
        self._vinkki_repository.create(nimi, url, tekija)

vinkki_service = VinkkiService()
