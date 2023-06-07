from rest_framework import serializers
from api_project.models import Project
from services import FabricService
from django.conf import settings
from api_project.serializers import TypeSerializer

class ProjectSerializer(serializers.ModelSerializer):
    type_projects = TypeSerializer(many=True)
    class Meta:
        model = Project
        fields = '__all__'
    
    def to_internal_value(self, data):
        data['user'] = self.context.get('request').user.id
        print("inside to internal value", data)
        return super().to_internal_value(data)

    def update(self, instance, validated_data):
        print('in update')
        return super().update(instance, validated_data)
    
    def create(self, validated_data):
        print("in create")
        return super().create(validated_data)
    
    def to_representation(self, instance):
        print('to_representation')
        print(settings.USE_HYPERLEDGER_FABRIC)  
        ret = super().to_representation(instance)
        action = self.context.get('view').action
        if action in ['create']:
            FabricService.addAsset(ret)
        # if action in ['list']:
        #     if not FabricService.isEqualHash(ret):
        #         ValueError("hash not match")
        elif action in ['update']:
            FabricService.updateAsset(ret)
        elif action in ['retrieve']:
            if not FabricService.isEqualHash(ret):
                ValueError("hash not match")
        return ret
    