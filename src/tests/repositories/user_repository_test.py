import unittest
from repositories.user_repository import (
    user_repository as default_user_repository
)

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        pass

    def test_find_by_username(self,username):
        result = default_user_repository.find_by_username(username)
        self.assertEqual(result[0],"testikayttaja")
        self.assertEqual(result[1],"pbkdf2:sha256:260000$rfkQEqTaTUMxWAEE$f1c39175079d3d5b38f3df47ca5fb98f90d2b7a0a1760a99639c74b373128bce")

    def test_create(self,username):
        pass