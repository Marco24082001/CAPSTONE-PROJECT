from rest_framework import serializers
from api_user.constants import Roles
from api_user.models import  User

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255)
    
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'first_name', 'last_name', 'full_name', 'role', 'avatar', 'biology', 'phone']
        extra_kwargs = {
            'avatar': {'required': False},
            'phone': {'required': False},
            'role': {'required': False},
            'birthday': {'required': False},
        }
    
    def create(self, validated_data):
        print(validated_data)
        return User.objects.create_user(**validated_data)
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        return ret
