from django.test import TestCase
from parameterized import parameterized_class

from hospital.models import Hospital
from hospital.models import Number
from map.models import Region

MAX_HOSPITAL_NAME_LENGTH = 100
MAX_HOSPITAL_FULL_ADDRESS_LENGTH = 150

MAX_NUMBER_PHONE_LENGTH = 25


@parameterized_class(
    ("name_location", "population", "name_hospital", "full_address"),
    [
        ("Berlin", 8000000.56, "Minsk Hospital №2", "st.Central 27, nm. 57"),
        ("Minsk", 750000.00, "Minsk Hospital №2", "st.Board 2, nm. 1"),
    ],
)
class HospitalModelTest(TestCase):
    def setUp(self):
        location = Region.objects.create(
            name=self.name_location, population=self.population
        )
        Hospital.objects.create(
            name=self.name_hospital, full_address=self.full_address, location=location
        )

    def test_validate_obj_representation(self):
        self.assertEquals(self.get_testing_hospital().__str__(), self.name_hospital)

    def test_validate_name(self):
        self.assertEquals(self.get_testing_hospital().name, self.name_hospital)

    def test_check_name_length(self):
        self.assertLessEqual(
            len(self.get_testing_hospital().name), MAX_HOSPITAL_NAME_LENGTH
        )

    def test_validate_full_address(self):
        self.assertEquals(self.get_testing_hospital().full_address, self.full_address)

    def test_check_full_address_length(self):
        self.assertLessEqual(
            len(self.get_testing_hospital().full_address),
            MAX_HOSPITAL_FULL_ADDRESS_LENGTH,
        )

    def get_testing_hospital(self):
        return Hospital.objects.get(name=self.name_hospital)


@parameterized_class(
    ("name_location", "population", "name_hospital", "full_address", "phone_number"),
    [
        (
            "Berlin",
            8000000.56,
            "Minsk Hospital №2",
            "st.Board 2, nm. 1",
            "+3752553364191",
        ),
        (
            "Minsk",
            750000.00,
            "Minsk Hospital №5",
            "st.Central 27, nm. 57",
            "+375255336477",
        ),
    ],
)
class NumberModelTest(TestCase):
    def setUp(self):
        location = Region.objects.create(
            name=self.name_location, population=self.population
        )
        hospital = Hospital.objects.create(
            name=self.name_hospital, full_address=self.full_address, location=location
        )
        Number.objects.create(number_phone=self.phone_number, hospital=hospital)

    def test_validate_obj_representation(self):
        self.assertEquals(self.get_testing_number().__str__(), self.phone_number)

    def test_validate_name(self):
        self.assertEquals(self.get_testing_number().number_phone, self.phone_number)

    def test_check_name_length(self):
        self.assertLessEqual(
            len(self.get_testing_number().number_phone), MAX_NUMBER_PHONE_LENGTH
        )

    def get_testing_number(self):
        return Number.objects.get(number_phone=self.phone_number)
