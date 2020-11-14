import logging
from hashlib import sha256

from django.test import TestCase

from client.models import Client
from client.models import Comment
from client.models import HosAdmin
from client.models import Status

MAX_USERNAME_LENGTH = 20
MIN_USERNAME_LENGTH = 4

MIN_PASSWORD_LENGTH = 4

USERNAME = "yauheni"
PASSWORD = "zs1919"
EMAIL = "zhenya@mail.ru"


class ClientModelTest(TestCase):
    def test_validate_obj_representation(self):
        self.assertEquals(self.get_testing_user().__str__(), USERNAME)

    def test_validate_username(self):
        self.assertEquals(self.get_testing_user().username, USERNAME)

    def test_check_username_length(self):
        self.assertGreaterEqual(
            len(self.get_testing_user().username), MIN_USERNAME_LENGTH
        ) and self.assertLessEqual(
            len(self.get_testing_user().username), MAX_USERNAME_LENGTH
        )

    def test_validate_password(self):
        self.assertEquals(self.get_testing_user().password, PASSWORD)

    def test_check_password_length(self):
        self.assertGreaterEqual(
            len(self.get_testing_user().password), MIN_PASSWORD_LENGTH
        )

    # def test_check_encrypt_password(self):
    #     user = self.get_testing_user()
    #     self.assertEquals(user.password, sha256(PASSWORD.encode("utf-8")).hexdigest())

    @classmethod
    def setUpTestData(cls):
        Client.objects.create(username=USERNAME, password=PASSWORD, email=EMAIL)

    @staticmethod
    def get_testing_user():
        return Client.objects.get(username=USERNAME)
