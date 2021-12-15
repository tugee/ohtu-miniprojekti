import unittest
from unittest.mock import Mock
from services.user_service import UserService

class TestUserService(unittest.TestCase):
    def setUp(self):
        mock_repo = Mock()
        service = UserService(mock_repo)

    def test_check_credentials(self):
        
        pass

    def test_create_user():
        pass
