from rest_framework import serializers
from api_project.models import Type
from services import FabricService
from api_base.exceptions import DataNotMatchHash

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

    def save(self, **kwargs):
        instance = super().save(**kwargs)
        FabricService.addAsset(self.data, Type.get_list_field_names())
        return instance
    
    def destroy(self, **kwargs):
        id = str(self.instance.id)
        self.instance.delete()
        FabricService.deleteAsset(id)
    
    def to_representation(self, instance):
        print('type to_representation')
        view = self.context.get('view')
        ret = super().to_representation(instance)
        if view and view.action in ['list', 'retrieve']:
            if not FabricService.isEqualHash(ret, Type.get_list_field_names()):
                raise DataNotMatchHash(instance.id, 'Transaction')
        return ret
