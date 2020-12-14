from subprocess import call

from django.contrib.sessions.models import Session
from django.test import Client as TestClient
from django.test import TestCase
from parameterized import parameterized_class

from client.models import Client
from client.models import HosAdmin
from client.models import Hospital

HOST = "127.0.0.1"
PORT = 8080
REGISTRATION_URL = "/registration/login/"
AUTHENTICATION_URL = "/registration/sign/"
LOGOUT_URL = "/registration/logout/"

MAP_URL = "/map"
HOSPITAL_URL = "/hospital"
REGION_URL = "/region"


@parameterized_class(
    (
        "username",
        "password",
        "email",
        "status",
        "is_admin",
        "region",
        "pagination_id",
        "hospital_id",
        "comment",
    ),
    [
        (
            "yauheni",
            "zs1919",
            "zhenya@mail.ru",
            1,
            "true",
            "mi",
            1,
            100,
            "Hello to everyone!!!",
        ),
        ("anton", "an1234", "anton@mail.ru", 1, "false", "vi", 2, 200, "Oh,yes..."),
    ],
)
class IntegrationTests(TestCase):
    """
    This class allows checking bound components in the website with different cases
    """

    fixtures = ["models.json"]

    @classmethod
    def setUpTestData(cls):
        cls.turn_off_server()
        cls.turn_on_server()

    def setUp(self):
        self.model = HosAdmin if self.is_admin == "true" else Client

        self.test_client = TestClient(enforce_csrf_checks=False)

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

    @staticmethod
    def turn_on_server():
        call("./run_server.sh {} {}".format(HOST, PORT), shell=True)

    @staticmethod
    def turn_off_server():
        call("./kill_sub.sh {}".format(PORT), shell=True)

    def get_request(self, url, params):
        return self.test_client.get(
            path="http://{}:{}{}".format(HOST, PORT, url), data=params
        )

    def post_request(self, url, params):
        return self.test_client.post(
            path="http://{}:{}{}".format(HOST, PORT, url), data=params, secure=False
        )

    def test_check_logged_user_in_system(self):
        # requests: 1.user registration 2.user authentication
        # that allows to checking redirect url(-s) and status(-es)
        self.assertEquals(self.registration_response.url, MAP_URL)
        self.assertEquals(self.authentication_response.url, MAP_URL)

        self.assertEquals(self.registration_response.status_code, 302)
        self.assertEquals(self.authentication_response.status_code, 302)

        # checking user session in cookies
        self.assertEquals(
            any(
                name.get_decoded().get(self.username, None)
                for name in Session.objects.all()
            ),
            True,
        )
        # creating a request to the logout url
        self.get_request(url=LOGOUT_URL, params={})

        # checking user session in cookies after logout
        self.assertEquals(
            any(
                name.get_decoded().get(self.username, None)
                for name in Session.objects.all()
            ),
            False,
        )

    def test_check_access_to_the_resource_after_auth(self):
        # requests: 1.user registration 2.user authentication
        # that allows to checking redirect url(-s) and status(-es)
        self.assertEquals(self.registration_response.url, MAP_URL)
        self.assertEquals(self.authentication_response.url, MAP_URL)

        self.assertEquals(self.registration_response.status_code, 302)
        self.assertEquals(self.authentication_response.status_code, 302)

        # checking user session in cookies
        self.assertEquals(
            any(
                name.get_decoded().get(self.username, None)
                for name in Session.objects.all()
            ),
            True,
        )
        # checking access after auth to the resource
        self.assertEquals(
            self.get_request(
                url="{}/{}/{}".format(REGION_URL, self.region, self.pagination_id),
                params={},
            ).status_code,
            200,
        )

    def test_check_comment_status(self):
        # requests: 1.user registration 2.user authentication
        # that allows to checking redirect url(-s) and status(-es)
        self.assertEquals(self.registration_response.url, MAP_URL)
        self.assertEquals(self.authentication_response.url, MAP_URL)

        self.assertEquals(self.registration_response.status_code, 302)
        self.assertEquals(self.authentication_response.status_code, 302)

        # checking user session in cookies
        self.assertEquals(
            any(
                name.get_decoded().get(self.username, None)
                for name in Session.objects.all()
            ),
            True,
        )

        # checking access after auth to the resource
        self.assertEquals(
            self.get_request(
                url="{}/{}".format(HOSPITAL_URL, self.hospital_id), params={}
            ).status_code,
            200,
        )

        # send a request that allows creating a comment on the web-page
        self.post_request(
            url="{}/{}".format(HOSPITAL_URL, self.hospital_id),
            params={"comment": self.comment},
        )
        # get comment using filtering in MTM database model with needed parameters
        comment = (
            Hospital.objects.all()
            .filter(id=self.hospital_id)
            .first()
            .comment_set.all()
            .filter(description=self.comment)
            .first()
            .description
        )

        # checking comment
        self.assertEquals(comment, self.comment)
