from django.db import models
from api_user.models import User
from api_project.models import Project
from api_base.models import BaseModel
from api_project.constants import TypeTransaction

class Transaction(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions", blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="transactions")
    message = models.TextField(null=True, blank=True)
    amount = models.FloatField(default=0)
    type_transaction = models.CharField(choices=TypeTransaction.choices(), default=TypeTransaction.INCREASE.value, max_length=50)
    is_anonymous = models.BooleanField(default=False)
    full_name = models.CharField(max_length=255, default="Anonymous", blank=True)

    fields_save_in_fabric = ['id', 'user', 'project', 'amount', 'type_transaction', 'is_anonymous', 'message']
    
    class Meta:
        db_table = "transactions"
        ordering = ('-created_at',)
