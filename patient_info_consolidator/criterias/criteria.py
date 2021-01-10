from abc import ABC, abstractmethod

class Criteria(ABC):
    def __init__(self, info: list):
        self.info = info

    @abstractmethod
    def calculate(self) -> float:
        """This take different values from the info list and returns a single value using the corresponding criteria"""


