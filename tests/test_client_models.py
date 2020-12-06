import re

from django.test import TestCase
from parameterized import parameterized_class

from client.models import Client
from client.models import HosAdmin

MAX_USERNAME_LENGTH = 20
MIN_USERNAME_LENGTH = 4
MIN_PASSWORD_LENGTH = 4
EMAIL_REGEX = r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*|^([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*|)@(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$"


@parameterized_class(
    ("username", "password", "email"),
    [("yauheni", "zs1919", "zhenya@mail.ru"), ("anton", "an1234ton", "anto@mail.com")],
)
class ClientModelTest(TestCase):
    def setUp(self):
        Client.objects.create(
            username=self.username, password=self.password, email=self.email
        )
        self.test_user = self.get_testing_user()

    def test_validate_obj_representation(self):
        self.assertEquals(self.test_user.__str__(), self.username)

    def test_validate_username(self):
        self.assertEquals(self.test_user.username, self.username)

    def test_check_username_length(self):
        self.assertGreaterEqual(
            len(self.test_user.username), MIN_USERNAME_LENGTH
        ) and self.assertLessEqual(len(self.test_user.username), MAX_USERNAME_LENGTH)

    def test_validate_password(self):
        self.assertEquals(self.test_user.password, self.password)

    def test_check_password_length(self):
        self.assertGreaterEqual(len(self.test_user.password), MIN_PASSWORD_LENGTH)

    def test_is_admin_user(self):
        self.assertEquals(self.test_user.is_admin, False)

    def get_testing_user(self):
        return Client.objects.get(username=self.username)


@parameterized_class(
    ("username", "password", "email"),
    [("ivan", "67iv49", "ivan@mail.ru"), ("den1", "den1den1", "den@mail.com")],
)
class HosAdminModelTest(TestCase):
    def setUp(self):
        HosAdmin.objects.create(
            username=self.username, password=self.password, email=self.email
        )
        self.test_user = self.get_testing_user()

    def test_validate_obj_representation(self):
        self.assertEquals(self.test_user.__str__(), self.username)

    def test_validate_username(self):
        self.assertEquals(self.test_user.username, self.username)

    def test_check_username_length(self):
        self.assertGreaterEqual(
            len(self.test_user.username), MIN_USERNAME_LENGTH
        ) and self.assertLessEqual(len(self.test_user.username), MAX_USERNAME_LENGTH)

    def test_check_mail(self):
        self.assertNotEqual(
            re.compile(EMAIL_REGEX, re.IGNORECASE).findall(self.email), []
        )

    def test_validate_password(self):
        self.assertEquals(self.test_user.password, self.password)

    def test_check_password_length(self):
        self.assertGreaterEqual(len(self.test_user.password), MIN_PASSWORD_LENGTH)

    def is_admin_user(self):
        self.assertEquals(self.test_user.is_admin, True)

    def get_testing_user(self):
        return HosAdmin.objects.get(username=self.username)
