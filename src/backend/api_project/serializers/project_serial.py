from rest_framework import serializers
from api_project.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
    
    def to_internal_value(self, data):
        data['user'] = self.context.get('request').user.id
        print("inside to internal value", data)
        return super().to_internal_value(data)

    def create(self, validated_data):
        print("in create", validated_data)
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        print("in update", validated_data)
        return super().update(instance, validated_data)
    
    def to_representation(self, instance):
        # print(super().to_representation(instance).description)
        raise ValueError("That word is not allowed here")
        return super().to_representation(instance)
    
