# Nirvana Home Challenge

Retrieves the patient data from different sources and consolidates the information applying different configurables criterias for each attribute


## Dependencies

* Python 3.8 or higher (older version may work but aren't tested)


## Initialize project

Run the following in order to enable the env and install dependencies:

```bash
python3 -m venv virtualenv
source virtualenv/bin/activate
pip install -r requirements.txt
```

## Try it

You may run an example code inside `example.py` running:

```bash
python example.py
```

## Run tests

You may run the tests for the entire package running:

```bash
python -m unittest -v tests
```

## Design

The idea behind the solution is to have 4 main components to retrieve the patient info, parse the info applying a criteria for each attribute and then create a model with that unified data.

The components are:

* Requester: is the responsible for retrieve all the information about a patient (identified by a `member_id`) from different sources and returning it in a list
* Parser: receives the list of patient info from the different sources and a detail of the attributes to be parsed (and the criteria to be applied for each one) and executes the corresponding calculations
* Criteria: different interchangeable pieces of code where each one defines the logic to be applied to calculate and consolidate the information of a particular attribute
* Model: the `PatientInfo` class defines a data structure that represents the information of a patient

### Adding a new Criteria

If you want to add a new Criteria, do the following:

1. Create a new criteria class in `patient_info_consolidator/criterias` folder who extends `Criteria` and applies a `calculate` method
2. Add a rule for initialize the new criteria in `CriteriaFactory.create_criteria`
3. Then, you can applies the new criteria in the PatientInfoParser setting the correct key in the attribute that you want


