import os
import re
from subprocess import call

import yaml
from django.contrib.sessions.models import Session
from django.test import Client as TestClient
from django.test import TestCase

from client.models import Client
from client.models import HosAdmin
from client.models import Region

HOST = "127.0.0.1"
PORT = 8080

REGISTRATION_URL = "/registration/login/"
AUTHENTICATION_URL = "/registration/sign/"

AVAILABLE_REGIONS = ["mi", "br", "mo", "vi", "gr", "go"]
MAP_URL = "/map"
HOSPITAL_URL = "/hospital"
REGION_URL = "/region"

MAX_USERNAME_LENGTH = 20
MIN_USERNAME_LENGTH = 4
MIN_PASSWORD_LENGTH = 4
EMAIL_REGEX = r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*|^([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*|)@(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$"

FUNCTION_NAME = "check_"


class MacBeinTest(TestCase):
    """
    This class allows checking bound components in the website with different cases
    """

    fixtures = ["models.json"]

    @classmethod
    def setUpTestData(cls):
        cls.turn_on_server()

        cls.params = yaml.safe_load(
            open("{}/tests/auth.yaml".format(os.path.abspath(os.getcwd())), "r")
        )

        cls.test_client = TestClient(enforce_csrf_checks=False)
        cls.turn_off_server()

    @staticmethod
    def turn_on_server():
        call("./run_server.sh {} {}".format(HOST, PORT), shell=True)

    @staticmethod
    def turn_off_server():
        call("./kill_sub.sh {}".format(PORT), shell=True)

    def test_cases(self):

        for function_name, function in MacBeinTest.__dict__.items():
            if function_name.startswith(FUNCTION_NAME):
                self.assertEquals(True, function(self))

    def check_params(self):
        if (
            not MIN_USERNAME_LENGTH
            < len(self.params["username"])
            <= MAX_USERNAME_LENGTH
        ):
            raise Exception("ERROR with username validation")
        elif not MIN_PASSWORD_LENGTH < len(self.params["password"]):
            raise Exception("ERROR with password validation")

        elif not re.compile(EMAIL_REGEX, re.IGNORECASE).findall(self.params["email"]):
            raise Exception("ERROR with email validation")

        else:
            print("check_params has finished successfully")
            return True

    def check_authentication(self):

        self.registration_response = self.post_request(
            params=self.params, url=REGISTRATION_URL
        )
        self.authentication_response = self.post_request(
            params=self.params, url=AUTHENTICATION_URL
        )

        if (
            self.registration_response.status_code != 302
            or self.registration_response.url != MAP_URL
        ):
            raise Exception("ERROR registration is failed")
        elif (
            self.authentication_response.status_code != 302
            or self.authentication_response.url != MAP_URL
        ):
            raise Exception("ERROR authentication is failed")
        else:
            print("check_authentication has finished successfully")
            return True

    def check_access_to_resources(self):
        self.authentication_response = self.post_request(
            params=self.params, url=AUTHENTICATION_URL
        )

        if (
            self.authentication_response.status_code != 302
            or self.authentication_response.url != MAP_URL
        ):
            raise Exception("ERROR registration is failed")

        elif self.get_request(url=MAP_URL, params={}).request["PATH_INFO"] != MAP_URL:
            raise Exception("ERROR map is inaccessible")
        # elif all(self.get_request(url='{}/{}/{}'.format(REGION_URL, region, 1), params={}) for region in
        #          AVAILABLE_REGIONS):
        #     pass
        else:
            print(
                self.get_request(
                    url="{}/{}/{}".format(REGION_URL, "mi", 1), params={}
                ).context
            )
            print("check_access_to_resources has finished successfully")
            return True

    def check_session(self):
        self.authentication_response = self.post_request(
            params=self.params, url=AUTHENTICATION_URL
        )
        if (
            self.authentication_response.status_code != 302
            or self.authentication_response.url != MAP_URL
        ):
            raise Exception("ERROR registration is failed")
        elif not any(
            name.get_decoded().get(self.params["username"], None)
            for name in Session.objects.all()
        ):
            raise Exception("ERROR user is not added in session")
        else:
            print("check_session has finished successfully")
            return True

    def get_request(self, url, params):
        return self.test_client.get(
            path="http://{}:{}{}".format(HOST, PORT, url), data=params
        )

    def post_request(self, url, params):
        return self.test_client.post(
            path="http://{}:{}{}".format(HOST, PORT, url), data=params, secure=False
        )
