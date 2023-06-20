from django.db import models
from api_base.models import BaseModel

class Type(BaseModel):
    name = models.CharField(default='', max_length=255)
    description = models.TextField()

    fields_save_in_fabric = ['id', 'name', 'description']
    
    class Meta:
        db_table = "types"
        ordering = ('-created_at',)
