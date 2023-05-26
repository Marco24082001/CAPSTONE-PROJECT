from django.db import models
from django.contrib.auth.models import AbstractUser
from api_base.models import BaseModel
from api_user.models import User
from api_project.models import Type
from api_project.constants import ProjectStatus


class Project(BaseModel, AbstractUser):
    title = models.CharField(max_length=255, default='')
    image_url = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    description = models.TextField()
    type_projects = models.ManyToManyField(blank=True, null=True, related_name='events', to=Type)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    fund_goal = models.FloatField(default=0)
    fund_total = models.FloatField(default=0)
    fund_used = models.FloatField(default=0)
    status = models.CharField(choices=ProjectStatus.choices(), default=ProjectStatus.DRAFT.value, max_length=50)

    class Meta:
        db_table = "projects"
        ordering = ('-created_at',)