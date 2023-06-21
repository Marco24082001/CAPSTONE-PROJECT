from api_base.views import BaseViewSet
from api_base.exceptions import DataNotMatchHash
from api_project.models import Type
from api_project.serializers import TypeSerializer
from rest_framework.response import Response
from rest_framework import status

class TypeViewSet(BaseViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(queryset, many=True)
        # call serializer.data to get data and check match in blockchain
        try:
            serializer.data
        except DataNotMatchHash as matchError:
            return Response(data= str(matchError), status=status.HTTP_302_FOUND)
        return Response(serializer.data)
    
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
    
