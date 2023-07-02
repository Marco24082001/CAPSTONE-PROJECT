from rest_framework import serializers
from api_project.models import Project
from services import FabricService
from api_project.serializers import TypeSerializer
from api_user.serializers import PublicUserSerializer
from api_base.exceptions import DataNotMatchHash
from datetime import datetime, date

class ProjectSerializer(serializers.ModelSerializer):
    list_types = TypeSerializer(source='type_projects', many=True, read_only=True)
    author = PublicUserSerializer(source='user', read_only=True)
    percent = serializers.SerializerMethodField(read_only=True)
    day_to_go = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Project
        fields = '__all__'
        extra_kwargs = {
            'full_name': {'required': False},
            'description': { 'required': False },
        }

    def to_internal_value(self, data):
        end_date = data.get('end_date')
        if end_date:
            datetime_obj = datetime.strptime(end_date, '%Y-%m-%dT%H:%M:%S.%fZ')
            end_date = datetime_obj.strftime('%Y-%m-%d')
            data['end_date'] = end_date    
        view = self.context.get('view')
        if view:
            data['user'] = self.context.get('request').user.id
        return super().to_internal_value(data)

    def get_percent(self, obj):
        return int((obj.fund_total/obj.fund_goal)*100)
    
    def get_day_to_go(self, obj):
        diff = obj.end_date - date.today()
        return diff.days
    
    def save(self, **kwargs):
        instance = super().save(**kwargs)
        FabricService.addAsset(self.data, Project.get_list_field_names())
        return instance
    
    def to_representation(self, instance):
        print(type(instance.id))
        view = self.context.get('view')
        ret = super().to_representation(instance)
        if view and view.action in ['retrieve']:
            if not FabricService.isEqualHash(ret, Project.get_list_field_names()):
                raise DataNotMatchHash(instance.id, 'Project')
        return ret
