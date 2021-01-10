from .average import AverageCriteria
from .criteria import Criteria
from .max import MaxCriteria
from .min import MinCriteria

class CriteriaFactory():
    def create_criteria(self, criteria: str, values: list) -> Criteria:
        if criteria == 'min':
            return MinCriteria(values)
        elif criteria == 'max':
            return MaxCriteria(values)
        return AverageCriteria(values)