from django.test import TestCase
from parameterized import parameterized_class

from map.models import Region

MAX_REGION_NAME_LENGTH = 30


@parameterized_class(
    ("name", "population"), [("Berlin", 8000000.56), ("Minsk", 750000.00)]
)
class RegionModelTest(TestCase):
    def setUp(self):
        Region.objects.create(name=self.name, population=self.population)

    def test_validate_obj_representation(self):
        self.assertEquals(self.get_testing_region().__str__(), self.name)

    def test_validate_name(self):
        self.assertEquals(self.get_testing_region().name, self.name)

    def test_check_name_length(self):
        self.assertLessEqual(
            len(self.get_testing_region().name), MAX_REGION_NAME_LENGTH
        )

    def test_validate_population(self):
        self.assertEquals(float(self.get_testing_region().population), self.population)

    def test_check_population_length(self):
        self.assertLessEqual(
            float(self.get_testing_region().population),
            float(format(self.population, ".2f")),
        ) and self.assertLessEqual(
            len(self.get_testing_region().population), len(str(self.population))
        )

    def get_testing_region(self):
        return Region.objects.get(name=self.name)
