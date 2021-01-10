from .criteria import Criteria

class MinCriteria(Criteria):
    def calculate(self) -> float:
        return min(self.info)