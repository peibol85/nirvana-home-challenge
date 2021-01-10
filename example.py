from patient_info_consolidator import PatientInfoRequester, PatientInfoParser, PatientInfo

def main():
    requester = PatientInfoRequester('index123')
    data = requester.get_results()
    parser = PatientInfoParser(
        {
            'attributes': { 'deductible': 'average', 'stop_loss': 'min', 'oop_max': 'max' },
            'info': data
        }
    )
    parsed_data = parser.execute()
    patient_info = PatientInfo(parsed_data)
    print(patient_info)
    
if __name__ == '__main__':
    main()