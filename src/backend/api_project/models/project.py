from django.db import models
from api_base.models import BaseModel
from api_user.models import User
from api_project.models import Type
from api_project.constants import ProjectStatus
from datetime import date

class Project(BaseModel):
    title = models.CharField(max_length=255, default='')
    image_url = models.CharField(max_length=255)
    description = models.TextField()
    type_projects = models.ManyToManyField(blank=True, related_name='projects', to=Type)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    fund_goal = models.FloatField(default=0)
    fund_total = models.FloatField(default=0)
    fund_used = models.FloatField(default=0)
    status = models.CharField(choices=ProjectStatus.choices(), default=ProjectStatus.ACTIVE.value, max_length=50)
    end_date = models.DateField()
    likes = models.ManyToManyField(
            User,
            related_name='user_likes',
            blank=True,
        )
    
    fields_save_in_fabric = ['id', 'title', 'image_url', 'description', 'user', 'fund_goal', 'fund_total', 'fund_used', 'status']

    
    class Meta:
        db_table = "projects"
        ordering = ('-created_at',)
