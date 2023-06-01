from rest_framework import serializers
from api_project.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
    
    def to_internal_value(self, data):
        # context
        print(self.context.get('request'))
        print("inside to internal value", data)
        return super().to_internal_value(data)

    def create(self, validated_data):
        print("in create", validated_data)
        # print("user")
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        print("in update", validated_data)
        return super().update(instance, validated_data)
