from rest_framework import serializers
from api_project.models import Type
from services import FabricService

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

    def save(self, **kwargs):
        instance = super().save(**kwargs)
        FabricService.addAsset(self.data, Type.get_list_field_names())
        return instance
    
    def to_representation(self, instance):
        print('to_representation')
        ret = super().to_representation(instance)
        if not FabricService.isEqualHash(ret, Type.get_list_field_names()):
                ValueError("hash not match")
        return ret
