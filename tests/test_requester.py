from unittest import TestCase
from patient_info_consolidator.requester import PatientInfoRequester

class TestPatientInfoRequester(TestCase):
    def test___init__(self):
        requester = PatientInfoRequester('123')
        self.assertEqual(requester.member_id, '123')
    
    def test_get_results(self):
        self.assertEqual(
            PatientInfoRequester('123').get_results(),
            [
                {'deductible': 1000, 'stop_loss': 10000, 'oop_max': 5000},
                {'deductible': 1200, 'stop_loss': 13000, 'oop_max': 6000},
                {'deductible': 1000, 'stop_loss': 10000, 'oop_max': 6000}
            ]
        )