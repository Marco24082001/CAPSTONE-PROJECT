from enum import Enum

class TypeTransaction(Enum):
    INCREASE = "INCREASE"
    DECREASE = "DECREASE"

    @classmethod
    def choices(cls):
        return ((i.name, i.value) for i in cls)
