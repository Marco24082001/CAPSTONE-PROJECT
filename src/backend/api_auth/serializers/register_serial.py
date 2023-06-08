from rest_framework import serializers
from api_base.models import BaseModel

# from api_auth.services import AccountService
from api_user.constants import Roles

from api_user.models import  User

class RegisterSerializer(BaseModel):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255)
    
    class Meta:
        model = User
        extra_kwargs = {
            'avatar': {'required': False},
            'phone': {'required': False},
            'role': {'required': False},
            'birthday': {'required': False},
        }
    
    def create(self, validated_data):
        User.objects


