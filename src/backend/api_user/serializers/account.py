from rest_framework import serializers
from api_user.models import Account


class AccountSerializer(serializers.ModelSerializer):
    # date_joined = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Account
        # fields = ['id', 'email', 'date_joined']
        fields = ['id', 'email']
    # def perform_create(self):
    # def create(self)
    def to_internal_value(self, data):
        return super().to_internal_value(data)

    def to_representation(self, instance):
        self.create()
        return super().to_representation(instance)
    # def create(self):
    #     super.create()