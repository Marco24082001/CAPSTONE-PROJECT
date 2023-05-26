from django.db import models
from api_base.models import BaseModel

class Type(BaseModel):
    fund_goal = models.FloatField(default=0)
    fund_total = models.FloatField(default=0)
    fund_used = models.FloatField(default=0)
    class Meta:
        db_table = "types"
        ordering = ('-created_at',)
