from schematics.models import Model
from schematics.types import FloatType


class PatientInfo(Model):
    deductible = FloatType(default=0)
    stop_loss = FloatType(default=0)
    oop_max = FloatType(default=0)

    def __repr__(self):
        return (
            f'PatientInfo(deductible={self.deductible}, stop_loss={self.stop_loss}, '
            f'oop_max={self.oop_max})'
        )