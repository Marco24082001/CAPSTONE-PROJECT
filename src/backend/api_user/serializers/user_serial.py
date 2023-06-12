from rest_framework import serializers
from api_user.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'first_name', 'last_name', 'full_name', 'role', 'avatar', 'biology', 'address', 'phone', 'birthday']
        extra_kwargs = {
            'full_name': {'required': False},
            'avatar': {'required': False},
            'phone': {'required': False},
            'birthday': {'required': False},
        }

    def create(self, validated_data):
        instance = self.Meta.model.objects.create_user(**validated_data)
        return instance

    def to_representation(self, instance):
        print('to_representation_user')
        return super().to_representation(instance)


class PublicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'full_name', 'avatar', 'biology']

    def to_representation(self, instance):
        print('author representation')
        return super().to_representation(instance)