from abc import ABC
from abc import abstractmethod

from django.test import TestCase

from client.models import Client
from client.models import HosAdmin

MAX_USERNAME_LENGTH = 20
MIN_USERNAME_LENGTH = 4

MIN_PASSWORD_LENGTH = 4

USERNAME = "yauheni"
PASSWORD = "zs1919"
EMAIL = "zhenya@mail.ru"


class UserTest(ABC):
    @abstractmethod
    def test_validate_obj_representation(self):
        pass

    @abstractmethod
    def test_validate_username(self):
        pass

    @abstractmethod
    def test_check_username_length(self):
        pass

    @abstractmethod
    def test_validate_password(self):
        pass

    @abstractmethod
    def test_check_password_length(self):
        pass

    @abstractmethod
    def is_admin_user(self):
        pass

    @staticmethod
    def get_testing_user(model):
        return model.objects.get(username=USERNAME)


class ClientModelTest(TestCase, UserTest):
    def setUp(self):
        Client.objects.create(username=USERNAME, password=PASSWORD, email=EMAIL)
        self.test_user = self.get_testing_user(Client)

    def test_validate_obj_representation(self):
        self.assertEquals(self.test_user.__str__(), USERNAME)

    def test_validate_username(self):
        self.assertEquals(self.test_user.username, USERNAME)

    def test_check_username_length(self):
        self.assertGreaterEqual(
            len(self.test_user.username), MIN_USERNAME_LENGTH
        ) and self.assertLessEqual(len(self.test_user.username), MAX_USERNAME_LENGTH)

    def test_validate_password(self):
        self.assertEquals(self.test_user.password, PASSWORD)

    def test_check_password_length(self):
        self.assertGreaterEqual(len(self.test_user.password), MIN_PASSWORD_LENGTH)

    def is_admin_user(self):
        self.assertEquals(self.test_user.is_admin, False)


class HosAdminModelTest(TestCase, UserTest):
    def setUp(self):
        HosAdmin.objects.create(username=USERNAME, password=PASSWORD, email=EMAIL)
        self.test_user = self.get_testing_user(HosAdmin)

    def test_validate_obj_representation(self):
        self.assertEquals(self.test_user.__str__(), USERNAME)

    def test_validate_username(self):
        self.assertEquals(self.test_user.username, USERNAME)

    def test_check_username_length(self):
        self.assertGreaterEqual(
            len(self.test_user.username), MIN_USERNAME_LENGTH
        ) and self.assertLessEqual(len(self.test_user.username), MAX_USERNAME_LENGTH)

    def test_validate_password(self):
        self.assertEquals(self.test_user.password, PASSWORD)

    def test_check_password_length(self):
        self.assertGreaterEqual(len(self.test_user.password), MIN_PASSWORD_LENGTH)

    def is_admin_user(self):
        self.assertEquals(self.test_user.is_admin, True)
