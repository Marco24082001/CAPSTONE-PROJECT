from enum import Enum

class ProjectStatus(Enum):
    DRAFT = "DRAFT"
    PUBLISHED = "PUBLISHED"
    DEACTIVATED = "DEACTIVATED"

    @classmethod
    def choices(cls):
        return ((i.name, i.value) for i in cls)
