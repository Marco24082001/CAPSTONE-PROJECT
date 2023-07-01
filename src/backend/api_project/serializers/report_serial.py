from rest_framework import serializers
from api_project.models import Report, Project
from services import FabricService
from api_project.serializers import ProjectSerializer
from api_base.exceptions import DataNotMatchHash

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

    def save(self, **kwargs):
        instance = super().save(**kwargs)
        FabricService.addAsset(self.data, Report.get_list_field_names())
        return instance

    def create(self, validated_data):
        # Update fund_used in project
        project = validated_data.get('project')
        amount = validated_data.get('amount')
        if (project.fund_total - amount) >= 0:
            instance = super().create(validated_data)
            fund_used = amount + project.fund_used
            project_serial = ProjectSerializer(project, data={ 'fund_used': fund_used}, partial=True)
            if project_serial.is_valid():
                project_serial.save()
            return instance
        else:
            ValueError

    def to_representation(self, instance):
        view = self.context.get('view')
        ret = super().to_representation(instance)
        if view and view.action in ['list', 'retrieve']:
            if not FabricService.isEqualHash(ret, Report.get_list_field_names()):
                raise DataNotMatchHash(instance.id, 'Report')
        return ret
