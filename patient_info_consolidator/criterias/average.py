from .criteria import Criteria

class AverageCriteria(Criteria):
    def calculate(self) -> float:
        return sum(self.info) / len(self.info)