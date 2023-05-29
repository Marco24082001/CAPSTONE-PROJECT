from api_base.views import BaseViewSet
from api_project.models import Type
from api_project.serializers import TypeSerializer

class TypeViewSet(BaseViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
