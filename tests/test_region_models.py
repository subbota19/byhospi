from django.test import TestCase

from map.models import Region

REGION_NAME = "Berlin"
POPULATION = 8000000.56

MAX_REGION_NAME_LENGTH = 30


class MapModelTest(TestCase):
    def setUp(self):
        Region.objects.create(name=REGION_NAME, population=POPULATION)

    def test_validate_obj_representation(self):
        self.assertEquals(self.get_testing_region().__str__(), REGION_NAME)

    def test_validate_name(self):
        self.assertEquals(self.get_testing_region().name, REGION_NAME)

    def test_check_name_length(self):
        self.assertLessEqual(
            len(self.get_testing_region().name), MAX_REGION_NAME_LENGTH
        )

    def test_validate_population(self):
        self.assertEquals(float(self.get_testing_region().population), POPULATION)

    def test_check_population_length(self):
        self.assertLessEqual(
            float(self.get_testing_region().population),
            float(format(POPULATION, ".2f")),
        ) and self.assertLessEqual(
            len(self.get_testing_region().population), len(str(POPULATION))
        )

    @staticmethod
    def get_testing_region():
        return Region.objects.get(name=REGION_NAME)
