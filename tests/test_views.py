from django.contrib.sessions.models import Session
from django_pyvows.context import DjangoHTTPContext
from parameterized import parameterized_class

from client.models import Client
from client.models import HosAdmin
from client.models import Region

WEBSITE_LOCALLY_ADDRESS = "127.0.0.1:8000"

REGISTRATION_URL = "registration/login/"
AUTHENTICATION_URL = "registration/sign/"

MAP_URL = "map"
HOSPITAL_URL = "hospital/"
REGION_URL = "region/"

# @parameterized_class(
#     ("username", "password", "email", "status", "is_admin"),
#     [("yauheni", "zs1919", "zhenya@mail.ru", 1, "true"),
#      ("anton", "an1234ton", "anto@mail.com", 2, "false")],
# )
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
