from unittest import TestCase
from patient_info_consolidator.criterias.min import MinCriteria

class TestMin(TestCase):
    def test___init__(self):
        criteria = MinCriteria([1000, 2000])
        self.assertEqual(criteria.info, [1000, 2000])

    def test_calculate(self):
        criteria = MinCriteria([1000, 2000])
        self.assertEqual(criteria.calculate(), 1000)