from django.db import models
from api_user.models import User
from api_project.models import Project
from api_base.models import BaseModel
from api_project.constants import TypeTransaction

class Report(BaseModel):
    title = models.CharField(max_length=255, default='')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="reports")
    description = models.TextField(null=True, blank=True)
    amount = models.FloatField(default=0)

    fields_save_in_fabric = ['id', 'title', 'project', 'amount', 'description']
    
    class Meta:
        db_table = "reports"
        ordering = ('-created_at',)
