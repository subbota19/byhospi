from django.test import TestCase

from hospital.models import Hospital
from hospital.models import Number
from map.models import Region

HOSPITAL_NAME = "Minsk Hospital №2"
HOSPITAL_FULL_ADDRESS = "st.Central 27, nm. 57"

MAX_HOSPITAL_NAME_LENGTH = 100
MAX_HOSPITAL_FULL_ADDRESS_LENGTH = 150

NUMBER_PHONE = "+3752553364191"
MAX_NUMBER_PHONE_LENGTH = 25


class HospitalModelTest(TestCase):
    def setUp(self):
        location = Region.objects.create(name="Random", population=1.00)
        Hospital.objects.create(
            name=HOSPITAL_NAME, full_address=HOSPITAL_FULL_ADDRESS, location=location
        )

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
            len(self.get_testing_hospital().full_address),
            MAX_HOSPITAL_FULL_ADDRESS_LENGTH,
        )

    @staticmethod
    def get_testing_hospital():
        return Hospital.objects.get(name=HOSPITAL_NAME)


class NumberModelTest(TestCase):
    def setUp(self):
        location = Region.objects.create(name="Random", population=1.00)
        hospital = Hospital.objects.create(
            name="Random", full_address="Random", location=location
        )
        Number.objects.create(number_phone=NUMBER_PHONE, hospital=hospital)

    def test_validate_obj_representation(self):
        self.assertEquals(self.get_testing_number().__str__(), NUMBER_PHONE)

    def test_validate_name(self):
        self.assertEquals(self.get_testing_number().number_phone, NUMBER_PHONE)

    def test_check_name_length(self):
        self.assertLessEqual(
            len(self.get_testing_number().number_phone), MAX_NUMBER_PHONE_LENGTH
        )

    @staticmethod
    def get_testing_number():
        return Number.objects.get(number_phone=NUMBER_PHONE)
