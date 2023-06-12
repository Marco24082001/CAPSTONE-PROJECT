from django.db import models
from django.db.models import Manager
from django.utils import timezone
import uuid


class BaseModel(models.Model):
    objects = Manager
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

    @classmethod
    def get_list_field_names(cls):
        list_field_names = [f.name for f in cls._meta.get_fields()]
        return list_field_names

