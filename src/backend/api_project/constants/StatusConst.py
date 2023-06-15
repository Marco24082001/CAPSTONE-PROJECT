from enum import Enum

class ProjectStatus(Enum):
    ACTIVE = "ACTIVE"
    FINISH = "FINISH"
    DEACTIVATED = "DEACTIVATED"

    @classmethod
    def choices(cls):
        return ((i.name, i.value) for i in cls)
