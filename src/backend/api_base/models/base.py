from django.db import models
from django.db.models import Manager
from django.utils import timezone
import uuid


class BaseModel(models.Model):
    fields_save_in_fabric = []
    objects = Manager
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

    @classmethod
    def get_list_field_names(cls):
        if not cls.fields_save_in_fabric:
            list_field_names = [f.name for f in cls._meta.get_fields()]
        else:
            list_field_names = cls.fields_save_in_fabric
        return list_field_names

