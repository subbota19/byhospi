import os
import re
from subprocess import call

import yaml
from django.contrib.sessions.models import Session
from django.test import Client as TestClient
from django.test import TestCase

from hospital.models import Hospital

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
MESSAGE = "test"
TEST_HOSPITAL_ID = 100
FUNCTION_NAME = "check_"


class MacBeinTest(TestCase):
    """
    This class allows checking bound components in the website with different cases
    """

    fixtures = ["models.json"]

    @classmethod
    def setUpTestData(cls):
        cls.turn_on_server()
        with open(
            "{}/tests/auth.yaml".format(os.path.abspath(os.getcwd())), "r"
        ) as file:
            cls.params = yaml.safe_load(file)

        cls.test_client = TestClient(enforce_csrf_checks=False)
        cls.turn_off_server()

    @staticmethod
    def turn_on_server():
        call("./run_server.sh {} {}".format(HOST, PORT), shell=True)

    @staticmethod
    def turn_off_server():
        call("./kill_sub.sh {}".format(PORT), shell=True)

    def test_cases(self):
        self.registration_response = self.post_request(
            params=self.params, url=REGISTRATION_URL
        )
        self.authentication_response = self.post_request(
            params=self.params, url=AUTHENTICATION_URL
        )

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
        if not MIN_PASSWORD_LENGTH < len(self.params["password"]):
            raise Exception("ERROR with password validation")

        if not re.compile(EMAIL_REGEX, re.IGNORECASE).findall(self.params["email"]):
            raise Exception("ERROR with email validation")

        print("check_params has finished successfully")
        return True

    def check_authentication(self):

        if (
            self.registration_response.status_code != 302
            or self.registration_response.url != MAP_URL
        ):
            raise Exception("ERROR registration is failed")
        if (
            self.authentication_response.status_code != 302
            or self.authentication_response.url != MAP_URL
        ):
            raise Exception("ERROR authentication is failed")

        print("check_authentication has finished successfully")
        return True

    def check_available_resources(self):

        if (
            self.get_request(url=MAP_URL, params={}).request["PATH_INFO"] != MAP_URL
            and self.get_request(url=MAP_URL, params={}).status_code == 200
        ):
            raise Exception("ERROR map is inaccessible")

        for region in AVAILABLE_REGIONS:
            if (
                self.get_request(
                    url="{}/{}/{}".format(REGION_URL, region, 1), params={}
                ).status_code
                != 200
            ):
                raise Exception("ERROR region is inaccessible")

        for hospital in Hospital.objects.all():
            if (
                self.get_request(
                    url="{}/{}".format(HOSPITAL_URL, hospital.id), params={}
                ).status_code
                != 200
            ):
                raise Exception("ERROR hospital(-s) is inaccessible")

        print("check_available_resources has finished successfully")
        return True

    def check_session(self):

        if (
            self.authentication_response.status_code != 302
            or self.authentication_response.url != MAP_URL
        ):
            raise Exception("ERROR registration is failed")
        if not any(
            name.get_decoded().get(self.params["username"], None)
            for name in Session.objects.all()
        ):
            raise Exception("ERROR user is not added in session")

        print("check_session has finished successfully")
        return True

    def check_message_and_description(self):

        if (
            self.authentication_response.status_code != 302
            or self.authentication_response.url != MAP_URL
        ):
            raise Exception("ERROR registration is failed")

        if not self.post_request(
            url="{}/{}".format(HOSPITAL_URL, TEST_HOSPITAL_ID),
            params={"description": MESSAGE},
        ):
            raise Exception("ERROR user can not add description")

        if not self.post_request(
            url="{}/{}".format(HOSPITAL_URL, TEST_HOSPITAL_ID),
            params={"comment": MESSAGE},
        ):
            raise Exception("ERROR user can not add comment")

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
