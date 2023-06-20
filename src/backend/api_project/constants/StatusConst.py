from enum import Enum

class ProjectStatus(Enum):
    ACTIVE = "ACTIVE"
    FINISHED = "FINISHED"
    INACTIVE = "INACTIVE"

    @classmethod
    def choices(cls):
        return ((i.name, i.value) for i in cls)
