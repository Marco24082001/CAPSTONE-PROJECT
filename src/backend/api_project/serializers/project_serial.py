from rest_framework import serializers
from api_project.models import Project
from services import FabricService
# from rest_framework import reverse
from api_project.serializers import TypeSerializer
from api_user.serializers import PublicUserSerializer

class ProjectSerializer(serializers.ModelSerializer):
    list_types = TypeSerializer(source="type_projects", many=True, read_only=True)
    author = PublicUserSerializer(source='user', read_only=True)
    # url = serializers.SerializerMethodField(read_only=True)
    percent = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Project
        fields = '__all__'
        extra_kwargs = {
            'full_name': {'required': False},
            'description': { 'required': False },
        }

    def to_internal_value(self, data):
        view = self.context.get('view')
        if view:
            data['user'] = self.context.get('request').user.id
        # print("inside to internal value", data)
        return super().to_internal_value(data)

    def get_percent(self, obj):
        return int((obj.fund_total/obj.fund_goal)*100)
    
    def save(self, **kwargs):
        print('project serializer save')
        instance = super().save(**kwargs)
        FabricService.addAsset(self.data, Project.get_list_field_names())
        return instance
    
    def to_representation(self, instance):
        print('to_representation')
        ret = super().to_representation(instance)
        if not FabricService.isEqualHash(ret, Project.get_list_field_names()):
                ValueError("hash not match")
        return ret
