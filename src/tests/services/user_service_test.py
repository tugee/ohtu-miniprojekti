import unittest
from services.user_service import UserService

class FakeUserRepository:
    def __init__(self):
        self.users = {}
    
    def find_by_username(self, username):
        return self.users[username]
    
    def create(self, username, password_hash):
        if username in self.users.keys():
            return
        self.users[username] = password_hash

class TestUserService(unittest.TestCase):
    def setUp(self):
        pass

    def test_luotu_kayttaja_menee_tietokantaan(self):
        fake_repo = FakeUserRepository()
        service = UserService(fake_repo)
        service.create_user("kayttaja", "salasana")
        self.assertTrue(fake_repo.users["kayttaja"])
        
