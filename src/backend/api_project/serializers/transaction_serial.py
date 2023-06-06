from rest_framework import serializers
from api_project.models import Transaction
from services import FabricService


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
    def update(self, instance, validated_data):
        print('in update')
        return super().update(instance, validated_data)
    
    def create(self, validated_data):
        print("in create")
        return super().create(validated_data)
    
    def to_representation(self, instance):
        print('to_representation')
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