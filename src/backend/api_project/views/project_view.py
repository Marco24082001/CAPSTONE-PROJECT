from api_base.views import BaseViewSet
from api_base.exceptions import DataNotMatchHash
from api_project.models import Project
from api_project.serializers import ProjectSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from api_project.constants import ProjectStatus
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from datetime import datetime, date

class ProjectViewSet(BaseViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    serializer_map = {}
    permission_map = {
        'upload_image': [AllowAny],
        'list': [AllowAny],
        'retrieve': [AllowAny],
        'get_project_owner': [AllowAny]
    }
    filterset_fields = ['status']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # logic change active to finish
        if instance.status == ProjectStatus.ACTIVE.value:
            diff = instance.end_date - date.today()
            if diff.days <= 0:
                serializer = self.get_serializer(instance, data={'status': ProjectStatus.FINISHED.value}, partial=True)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)
                return Response(serializer.data)
        serializer = self.get_serializer(instance)
        try:
            serializer.data
        except DataNotMatchHash as matchError:
            return Response(data= str(matchError), status=status.HTTP_302_FOUND)
        return Response(serializer.data)

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
    
    @action(detail=False, methods=['POST'])
    def upload_image(self, request, *args):
        return Response(data=None, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['GET'])
    def get_project_owner(self, request, *args):
        user_id = request.query_params.get('user_id', None)
        print(user_id)
        if not user_id:
            return Response(data=status.HTTP_400_BAD_REQUEST)
        # owner = self.request.user
        queryset = Project.objects.filter(user=user_id)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    @swagger_auto_schema(method='PUT', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'status': openapi.Schema(type=openapi.TYPE_STRING, default=ProjectStatus.INACTIVE.value),
        })
    )
    @action(detail=True, methods=['PUT'])
    def deactivate(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data={ 'status' : ProjectStatus.INACTIVE.value}, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)
    
    @action(detail=True, methods=['PUT'])
    def activate(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data={ 'status' : ProjectStatus.ACTIVE.value}, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)
    
    @action(detail=False, methods=['GET'])
    def getLikeProjects(self, request, *args, **kwargs):
        user = self.request.user
        queryset = Project.objects.filter(likes__id=user.id)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
