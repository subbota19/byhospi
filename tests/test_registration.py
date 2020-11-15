import requests
from django.test import Client as TestClient
from django.test import TestCase

from client.models import Client
from client.models import HosAdmin

WEBSITE_LOCALLY_ADDRESS = "127.0.0.1:8000"
REGISTRATION_URL = "registration/login/"

USERNAME = "yauheni"
PASSWORD = "zs1919"
EMAIL = "zhenya@mail.ru"
STATUS = 1


class RegistrationTest(TestCase):
    def setUp(self):
        self.create_post_request()

    def test_check_logged_user_in_system(self):
        self.assertEquals(self.response.status_code, 200)

        print(self.response.url)

    def create_post_request(self):
        params = {
            "username": USERNAME,
            "password": PASSWORD,
            "email": EMAIL,
            "is_admin": "Client",
            "status": STATUS,
        }

        test_client = TestClient(enforce_csrf_checks=False)

        self.response = test_client.post(
            path="http://{}/{}".format(WEBSITE_LOCALLY_ADDRESS, REGISTRATION_URL),
            data=params,
            secure=False,
        )
