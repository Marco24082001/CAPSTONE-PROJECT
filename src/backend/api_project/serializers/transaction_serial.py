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
    
    def to_internal_value(self, data):
        is_anonymous = data['is_anonymous']
        if not is_anonymous:
            user = self.context.get('request').user
            data['user'] = user.id if user else None
        else:
            data['full_name'] = "Anonymous"
        return super().to_internal_value(data)
    
    def create(self, validated_data):
        instance = super().create(validated_data)
        # Update total, likes, status in project
        project = instance.project
        fund_total = project.fund_total + instance.amount
        print(project.likes)
        likes = []
        for like in project.likes.all():
            likes.append(str(like.id))
        if instance.user: likes.append(str(instance.user.id))
        data = {
            'fund_total': fund_total,
            'likes': likes,
        }
        if fund_total >= project.fund_goal:
            data['status'] = 'FINISHED'
        project_serial = ProjectSerializer(project, data=data, partial=True)
        if project_serial.is_valid():
            project_serial.save()
        return instance
    
    def to_representation(self, instance):
        print('to_representation')
        ret = super().to_representation(instance)
        if not FabricService.isEqualHash(ret, Transaction.get_list_field_names()):
                ValueError("hash not match")
        if ret['user']:
            ret['full_name'] = ret['supporter']['full_name']
        # action = self.context.get('view').action
        return ret

