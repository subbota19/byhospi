from django.test import TestCase

from client.models import Client
from client.models import Comment
from client.models import HosAdmin
from client.models import Status


class ClientModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Client.objects.create(
            username="yauheni", password="zs1919", email="zhenya@mail.ru"
        )

    def test_validate_username(self):
        client = Client.objects.get(username="yauheni")
        self.assertEquals(client.username, "yauheni")

    def test_validate_obj_representation(self):
        client = Client.objects.get(username="yauheni")
        self.assertEquals(client.__str__(), "yauheni")