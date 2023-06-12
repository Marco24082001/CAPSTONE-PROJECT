from django.db import models
from api_user.models import User
from api_project.models import Project
from api_base.models import BaseModel
from api_project.constants import TypeTransaction

class Transaction(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="transactions")
    description = models.TextField()
    amount = models.FloatField(default=0)
    type_transaction = models.CharField(choices=TypeTransaction.choices(), default=TypeTransaction.INCREASE.value,
                                        max_length=50)
    
    class Meta:
        db_table = "transactions"
        ordering = ('-created_at',)
    