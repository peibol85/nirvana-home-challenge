from unittest import TestCase
from patient_info_consolidator.criterias import CriteriaFactory
from patient_info_consolidator.criterias.average import AverageCriteria
from patient_info_consolidator.criterias.criteria import Criteria
from patient_info_consolidator.criterias.max import MaxCriteria
from patient_info_consolidator.criterias.min import MinCriteria

class TestCriteriaFactory(TestCase):
    def test_create_criteria(self):
        values = [1000, 2000]
        self.assertIsInstance(
            CriteriaFactory().create_criteria('average', values),
            Criteria
        )
        self.assertIsInstance(
            CriteriaFactory().create_criteria('average', values),
            AverageCriteria
        )
        self.assertIsInstance(
            CriteriaFactory().create_criteria('min', values),
            MinCriteria
        )
        self.assertIsInstance(
            CriteriaFactory().create_criteria('max', values),
            MaxCriteria
        )
        self.assertIsInstance(
            CriteriaFactory().create_criteria('anything', values),
            AverageCriteria
        )