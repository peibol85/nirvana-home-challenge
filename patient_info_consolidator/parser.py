from schematics.models import Model
from schematics.types import DictType, IntType, StringType, ListType
from collections import defaultdict
from .criterias import CriteriaFactory

class PatientInfoParser(Model):
    attributes = DictType(StringType)
    info = ListType(DictType(IntType))

    def execute(self) -> dict:
        # Initializes the dict for the operations
        values = defaultdict(list)
        patient_values = dict.fromkeys(self.attributes.keys(), 0) # pylint: disable=no-member
        # Creates a dict with the list of values for each attribute
        for item in self.info: # pylint: disable=not-an-iterable
            for key in item.keys():
                values[key].append(item[key])
        # Applies the correct criteria for each attribute
        for attribute, criteria in self.attributes.items(): # pylint: disable=no-member
            if attribute in values.keys():
                concrete_criteria = CriteriaFactory().create_criteria(criteria, values[attribute])
                patient_values[attribute] = concrete_criteria.calculate()
        return patient_values