from rest_framework import serializers
from api_project.models import Type
from services import FabricService

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

    def update(self, instance, validated_data):
        print('in update')
        return super().update(instance, validated_data)
    
    def create(self, validated_data):
        print("in create")
        return super().create(validated_data)
    
    def to_representation(self, instance):
        # print('type vothanvi')
        print('to_representation_type')
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
    