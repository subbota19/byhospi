import logging

from django.test import TestCase

from client.models import Client
from client.models import Comment
from client.models import HosAdmin
from client.models import Status

MAX_USERNAME_LENGTH = 20
MIN_USERNAME_LENGTH = 4

MIN_PASSWORD_LENGTH = 4


class ClientModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Client.objects.create(
            username="yauheni", password="zs1919", email="zhenya@mail.ru"
        )

    def test_validate_obj_representation(self):
        self.assertEquals(self.get_testing_user().__str__(), "yauheni")

    def test_validate_username(self):
        self.assertEquals(self.get_testing_user().username, "yauheni")

    def test_check_username_length(self):
        self.assertGreaterEqual(
            len(self.get_testing_user().username), MIN_USERNAME_LENGTH
        ) and self.assertLessEqual(
            len(self.get_testing_user().username), MAX_USERNAME_LENGTH
        )

    def test_validate_password(self):
        self.assertEquals(self.get_testing_user().password, "zs1919")

    def test_check_password_length(self):
        self.assertGreaterEqual(
            len(self.get_testing_user().password), MIN_PASSWORD_LENGTH
        )

    @staticmethod
    def get_testing_user():
        logging.info(Client.objects.get(username="yauheni").password)
        return Client.objects.get(username="yauheni")
