from rest_framework import serializers
from api_project.models import Transaction
from api_project.models import Project
from services import FabricService
from api_user.serializers import PublicUserSerializer
from api_project.serializers.project_serial import ProjectSerializer


class TransactionSerializer(serializers.ModelSerializer):
    supporter = PublicUserSerializer(source='user', read_only=True)
    class Meta:
        model = Transaction
        fields = '__all__'

    def save(self, **kwargs):
        instance = super().save(**kwargs)
        FabricService.addAsset(self.data, Transaction.get_list_field_names())
        return instance
    
    def create(self, validated_data):
        instance = super().create(validated_data)
        # Update total in project
        project = instance.project
        fund_total = project.fund_total + instance.amount
        project_serial = ProjectSerializer(project, data= {
             'fund_total': fund_total, 
        }, partial=True)
        if project_serial.is_valid():
            project_serial.save()
        return instance
    
    def to_representation(self, instance):
        print('to_representation')
        ret = super().to_representation(instance)
        if not FabricService.isEqualHash(ret, Transaction.get_list_field_names()):
                ValueError("hash not match")

        # action = self.context.get('view').action
        # if action in ['create']:
        #     FabricService.addAsset(ret)
        # if action in ['list']:
        #     if not FabricService.isEqualHash(ret):
        #         ValueError("hash not match")
        # elif action in ['update']:
        #     FabricService.updateAsset(ret)
        # elif action in ['retrieve']:
        #     if not FabricService.isEqualHash(ret):
        #         ValueError("hash not match")
        return ret

