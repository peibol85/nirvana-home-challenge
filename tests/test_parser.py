from unittest import TestCase
from patient_info_consolidator.parser import PatientInfoParser

class TestPatientInfoParser(TestCase):
    def test___init__(self):
        parser = PatientInfoParser(
            {
                'attributes': { 'one': 'average', 'two': 'min', 'three': 'max' },
                'info': [
                    {'one': 1000, 'two': 2000, 'three': 3000},
                    {'one': 10000, 'two': 20000, 'three': 30000},
                ]
            }
        )
        self.assertEqual(parser.attributes, { 'one': 'average', 'two': 'min', 'three': 'max' })
        self.assertEqual(parser.info, [
            {'one': 1000, 'two': 2000, 'three': 3000},
            {'one': 10000, 'two': 20000, 'three': 30000},
        ])
    
    
    def test_execute(self):
        parser = PatientInfoParser(
            {
                'attributes': { 'one': 'average', 'two': 'min', 'three': 'max' },
                'info': [
                    {'one': 1000, 'two': 2000, 'three': 3000},
                    {'one': 10000, 'two': 20000, 'three': 30000},
                ]
            }
        )
        self.assertEqual(
            parser.execute(),
            {'one': 5500, 'two': 2000, 'three': 30000}
        )
        parser2 = PatientInfoParser(
            {
                'attributes': { 'one': 'average', 'two': 'min', 'three': 'max', 'four': 'average' },
                'info': [
                    {'one': 1000, 'two': 2000, 'three': 3000},
                    {'one': 10000, 'two': 20000, 'three': 30000},
                ]
            }
        )
        self.assertEqual(
            parser2.execute(),
            {'one': 5500, 'two': 2000, 'three': 30000, 'four': 0}
        )
        parser3 = PatientInfoParser(
            {
                'attributes': { 'one': 'average', 'two': 'min' },
                'info': [
                    {'one': 1000, 'two': 2000, 'three': 3000},
                    {'one': 10000, 'two': 20000, 'three': 30000},
                ]
            }
        )
        self.assertEqual(
            parser3.execute(),
            {'one': 5500, 'two': 2000}
        )