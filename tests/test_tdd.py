from subprocess import call

from bs4 import BeautifulSoup
from django.test import Client as TestClient
from django.test import TestCase

from map.models import Region
from service import map

HOST = "127.0.0.1"
PORT = 8080

MAP_URL = "/map"
CHECK_FIELD = "official_link"
CHECK_REGION = "mi"

FUNCTION_NAME = "check_"


class ImplementMapFeatureTest(TestCase):
    fixtures = ["models.json"]

    @classmethod
    def setUpTestData(cls):
        cls.test_client = TestClient(enforce_csrf_checks=False)
        cls.turn_off_server()
        cls.turn_on_server()

    @staticmethod
    def turn_on_server():
        call("./run_server.sh {} {}".format(HOST, PORT), shell=True)

    @staticmethod
    def turn_off_server():
        call("./kill_sub.sh {}".format(PORT), shell=True)

    def test_cases(self):

        for function_name, function in ImplementMapFeatureTest.__dict__.items():
            if function_name.startswith(FUNCTION_NAME):
                bool_result = function(self)
                self.assertEquals(True, bool_result)
                print("Test - {}; Result - {}".format(function, bool_result))

    def check_fields(self):
        return bool(
            {field.name: field for field in Region._meta.fields}.get(CHECK_FIELD, False)
        )

    def check_main_page(self):
        html_map = self.get_request(url=MAP_URL, params={})
        return all(self.parse_page(html_map.__dict__["_container"][0].decode("utf-8")))

    @staticmethod
    def parse_page(html_page: str) -> list:
        bs4_obg = BeautifulSoup(html_page, "html.parser")
        list_checker = []
        for region in (
            bs4_obg.find("div", {"class", "by_map"}).find("svg").find_all("path")
        ):
            list_checker.append(region.get(CHECK_FIELD, False))

        return list_checker

    def get_request(self, url, params):
        return self.test_client.get(
            path="http://{}:{}{}".format(HOST, PORT, url), data=params
        )

    def post_request(self, url, params):
        return self.test_client.post(
            path="http://{}:{}{}".format(HOST, PORT, url), data=params, secure=False
        )


class ImplementHospitalFilterFeatureTest(TestCase):
    fixtures = ["models.json"]

    @classmethod
    def setUpTestData(cls):
        cls.turn_on_server()
        cls.test_client = TestClient(enforce_csrf_checks=False)
        cls.turn_off_server()

    @staticmethod
    def turn_on_server():
        call("./run_server.sh {} {}".format(HOST, PORT), shell=True)

    @staticmethod
    def turn_off_server():
        call("./kill_sub.sh {}".format(PORT), shell=True)

    def test_cases(self):

        for (
            function_name,
            function,
        ) in ImplementHospitalFilterFeatureTest.__dict__.items():
            if function_name.startswith(FUNCTION_NAME):
                bool_result = function(self)
                self.assertEquals(True, bool_result)
                print("Test - {}; Result - {}".format(function, bool_result))

    def check_hospital_order(self):
        switch = 1
        count_page = 1
        while True:
            hospitals = map.get_regions_by_name_and_id(
                region=CHECK_REGION, page=count_page
            )["hospitals"]
            if not hospitals:
                break
            for hospital in hospitals:
                if hospital.need_help and switch == 0:
                    return False
                if not hospital.need_help:
                    switch = 0
            count_page += 1
        return True

    def get_request(self, url, params):
        return self.test_client.get(
            path="http://{}:{}{}".format(HOST, PORT, url), data=params
        )

    def post_request(self, url, params):
        return self.test_client.post(
            path="http://{}:{}{}".format(HOST, PORT, url), data=params, secure=False
        )
