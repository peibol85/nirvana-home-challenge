from unittest import TestCase
from patient_info_consolidator.criterias.average import AverageCriteria

class TestAverage(TestCase):
    def test___init__(self):
        criteria = AverageCriteria([1000, 2000])
        self.assertEqual(criteria.info, [1000, 2000])

    def test_calculate(self):
        criteria = AverageCriteria([1000, 2000])
        self.assertEqual(criteria.calculate(), 1500)