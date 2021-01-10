import os
import json


class PatientInfoRequester():
    member_id = ''

    def __init__(self, member_id: str):
        self.member_id = member_id

    def get_results(self) -> dict:
        mocksDir = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + '/../mocks')
        data = []
        for index in range(1, 4):
            with open(mocksDir + f'/api{str(index)}.json') as f:
                data.append(json.load(f))
        return data