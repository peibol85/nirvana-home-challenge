from unittest import TestCase
from patient_info_consolidator.criterias.max import MaxCriteria

class TestMax(TestCase):
    def test___init__(self):
        criteria = MaxCriteria([1000, 2000])
        self.assertEqual(criteria.info, [1000, 2000])

    def test_calculate(self):
        criteria = MaxCriteria([1000, 2000])
        self.assertEqual(criteria.calculate(), 2000)