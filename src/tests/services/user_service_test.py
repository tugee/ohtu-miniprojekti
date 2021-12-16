import unittest
from unittest.mock import Mock
from werkzeug.security import generate_password_hash
#from app import db
from services.user_service import UserService

class TestUserServiceClass(unittest.TestCase):
    def setUp(self) -> None:
        self.user_repo_mock = Mock()
        self.user_model_mock = Mock()

        self.user_repo_mock.find_by_username.side_effect = [
            None,
            ('kayttaja', generate_password_hash('salasana', method='sha256'))
        ]

        self.user_service = UserService(self.user_repo_mock)

    def test_check_credentials_checks_for_username(self):
        self.user_service.check_credentials('kayttaja', 'salasana')
        self.user_repo_mock.find_by_username.assert_called_with('kayttaja')

    def test_check_credentials_returns_none_if_not_user(self):
        result = self.user_service.check_credentials('kayttaja', 'salasana')
        self.assertIsNone(result)

    def test_check_credentials_returns_valid_user(self):
        self.user_service.check_credentials('kayttaja', 'salasana')
        result = self.user_service.check_credentials('kayttaja', 'salasana')
        self.assertIsNotNone(result)

    def test_create_user_works(self):
        self.user_service.create_user("kayttaja", "salasana")
        self.user_repo_mock.create.assert_called()        