from repositories.vinkki_repository import (
    vinkki_repository as default_vinkki_repository
)

class VinkkiService:
    def __init__(self, vinkki_repository=default_vinkki_repository):
        self._vinkki_repository = vinkki_repository

    def search_vinkkis(self):
        vinkit = self._vinkki_repository.find_by_vinkki()
        return vinkit

    def search_own_vinkkis(self, tekija):
        vinkit = self._vinkki_repository.find_by_user(tekija)
        return vinkit

    def create_vinkki(self, nimi, url, tekija):
        self._vinkki_repository.create(nimi, url, tekija)

    def hide_vinkki(self, nimi):
        self._vinkki_repository.hide(nimi)

    def set_read_vinkki(self, vinkki_id):
        self._vinkki_repository.set_read(vinkki_id)
        self._vinkki_repository.set_read_date(vinkki_id)

    def set_unread_vinkki(self, vinkki_id):
        self._vinkki_repository.set_unread(vinkki_id)

vinkki_service = VinkkiService()
