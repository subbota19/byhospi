from subprocess import call

from django.contrib.sessions.models import Session
from django.test import Client as TestClient
from django.test import TestCase
from parameterized import parameterized_class

from client.models import Client
from client.models import HosAdmin
from client.models import Region

HOST = "127.0.0.1"
PORT = 8080
REGISTRATION_URL = "/registration/login/"
AUTHENTICATION_URL = "/registration/sign/"

MAP_URL = "/map"
HOSPITAL_URL = "/hospital/"
REGION_URL = "/region/"


@parameterized_class(
    ("username", "password", "email", "status", "is_admin"),
    [
        (
            "yauheni",
            "zs1919",
            "zhenya@mail.ru",
            1,
            "true",
        ),
        ("anton", "an1234", "anton@mail.ru", 1, "false"),
    ],
)
class ViewsTests(TestCase):
    """
    This class allows checking bound components in the website with different cases
    """

    fixtures = ["models.json"]

    def setUp(self):
        self.model = HosAdmin if self.is_admin == "true" else Client

        self.test_client = TestClient(enforce_csrf_checks=False)

        call("./run_server.sh {} {}".format(HOST, PORT), shell=True)

        self.registration_response = self.post_request(
            params={
                "username": self.username,
                "password": self.password,
                "email": self.email,
                "is_admin": self.model,
                "status": self.status,
            },
            url=REGISTRATION_URL,
        )
        self.authentication_response = self.post_request(
            params={
                "username": self.username,
                "password": self.password,
                "is_admin": self.model,
            },
            url=AUTHENTICATION_URL,
        )

    @classmethod
    def tearDownClass(cls):
        call("./kill_sub.sh {}".format(PORT), shell=True)
        super(TestCase, cls).tearDownClass()

    def get_request(self, url, params):
        return self.test_client.get(
            path="http://{}:{}{}".format(HOST, PORT, url), data=params
        )

    def post_request(self, url, params):
        return self.test_client.post(
            path="http://{}:{}{}".format(HOST, PORT, url), data=params, secure=False
        )

    def test_check_logged_user_in_system(self):
        self.assertEquals(self.registration_response.url, MAP_URL)

        self.assertEquals(self.authentication_response.url, MAP_URL)

    def test_check_user_status(self):
        self.assertEquals(self.registration_response.status_code, 302)

        self.assertEquals(self.authentication_response.status_code, 302)

    def test_check_session(self):
        self.assertEquals(
            any(
                name.get_decoded().get(self.username, None)
                for name in Session.objects.all()
            ),
            True,
        )

    def test_map_view_status_code(self):
        self.assertEquals(self.get_request(url=MAP_URL, params={}).status_code, 200)

    def test_map_view_url(self):
        self.assertEquals(
            self.get_request(url=MAP_URL, params={}).request["PATH_INFO"], MAP_URL
        )


# class MapView(DjangoHTTPContext):
#     def setUp(self):
#         self.model = HosAdmin if self.is_admin == 'true' else Client
#         self.test_client = TestClient(enforce_csrf_checks=False)
#
#         self.registration_response = self.post_request(
#             params={
#                 "username": self.username,
#                 "password": self.password,
#                 "email": self.email,
#                 "is_admin": self.model,
#                 "status": self.status,
#             }, url=REGISTRATION_URL)
#         self.authentication_response = self.post_request(
#             params={
#                 "username": self.username,
#                 "password": self.password,
#                 "is_admin": self.model,
#             }, url=AUTHENTICATION_URL)
#
#     def post_request(self, params, url):
#         return self.test_client.post(path="http://{}/{}".format(WEBSITE_LOCALLY_ADDRESS, url),
#                                      data=params, secure=False)
#
#     def get_request(self, params, url):
#         return self.test_client.get(path="http://{}/{}".format(WEBSITE_LOCALLY_ADDRESS, url), data=params)
#
#     def test_check_logged_user_in_system(self):
#         self.assertEquals(self.registration_response.url, '/map')
#
#         self.assertEquals(self.authentication_response.url, '/map')
#
#     def test_check_user_status(self):
#         self.assertEquals(self.registration_response.status_code, 302)
#
#         self.assertEquals(self.authentication_response.status_code, 302)
#
#     def test_check_session(self):
#         self.assertEquals(any(name.get_decoded().get(self.username, None) for name in Session.objects.all()), True)
#
#     def test_map_view(self):
#         pass
#
#     def test_region_view(self):
#         pass
#
#     def test_hospital_view(self):
#         pass
#
#     def test_check_map_status(self):
#         Region.objects.create(name="Minsk", population=100)
#         self.assertEquals(self.get_request(params={}, url=MAP_URL).status_code, 200)
#
# def test_check_region_status(self):
#     self.assertEquals(self.get_request(params=None, url=REGION_URL).status_code, 200)
#
# def test_check_hospital_status(self):
#     self.assertEquals(self.get_request(params=None, url=HOSPITAL_URL).status_code, 200)
