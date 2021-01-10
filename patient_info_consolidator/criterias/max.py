from .criteria import Criteria

class MaxCriteria(Criteria):
    def calculate(self) -> float:
        return max(self.info)