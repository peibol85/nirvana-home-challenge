from unittest import TestCase
from patient_info_consolidator import PatientInfo

class TestPatientInfo(TestCase):
    def test___init__(self):
        patient = PatientInfo({ 'deductible': 1000, 'stop_loss': 2000, 'oop_max': 3000 })
        self.assertEqual(patient.deductible, 1000)
        self.assertEqual(patient.stop_loss, 2000)
        self.assertEqual(patient.oop_max, 3000)

    def test___repr__(self):
        patient = PatientInfo({ 'deductible': 1000, 'stop_loss': 2000, 'oop_max': 3000 })
        self.assertEqual(patient.__repr__(), 'PatientInfo(deductible=1000.0, stop_loss=2000.0, oop_max=3000.0)')