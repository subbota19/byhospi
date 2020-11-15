from django.test import TestCase

from hospital.models import Hospital
from hospital.models import Number

HOSPITAL_NAME = "Minsk Hospital №1"
HOSPITAL_FULL_ADDRESS = "st.Central 27, nm. 60"

MAX_HOSPITAL_NAME_LENGTH = 100
MAX_HOSPITAL_FULL_ADDRESS_LENGTH = 150


class MapModelTest(TestCase):
    def setUp(self):
        Hospital.objects.create(name=HOSPITAL_NAME, full_address=HOSPITAL_FULL_ADDRESS)

    def test_validate_obj_representation(self):
        self.assertEquals(self.get_testing_hospital().__str__(), HOSPITAL_NAME)

    def test_validate_name(self):
        self.assertEquals(self.get_testing_hospital().name, HOSPITAL_NAME)

    def test_check_name_length(self):
        self.assertLessEqual(
            len(self.get_testing_hospital().name), MAX_HOSPITAL_NAME_LENGTH
        )

    def test_validate_full_address(self):
        self.assertEquals(
            self.get_testing_hospital().full_address, HOSPITAL_FULL_ADDRESS
        )

    def test_check_full_address_length(self):
        self.assertLessEqual(
            self.get_testing_hospital().full_address, MAX_HOSPITAL_FULL_ADDRESS_LENGTH
        )

    @staticmethod
    def get_testing_hospital():
        return Hospital.objects.get(name=HOSPITAL_NAME)
