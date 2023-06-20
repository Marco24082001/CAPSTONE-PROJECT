from api_base.views import BaseViewSet
from api_project.models import Type
from api_project.serializers import TypeSerializer
from rest_framework.response import Response
from rest_framework import status

class TypeViewSet(BaseViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    
    def destroy(self, request, *args, **kwargs):     
        instance = self.get_object()
        # check if this type is used
        projects = instance.projects.all()
        if not projects:
            serializer = self.get_serializer(instance)
            serializer.destroy()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_409_CONFLICT, data={ 'error': "This type is used" })
 