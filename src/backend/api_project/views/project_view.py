from api_base.views import BaseViewSet
from api_project.models import Project
from api_project.serializers import ProjectSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from api_project.constants import ProjectStatus
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class ProjectViewSet(BaseViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    serializer_map = {}
    permission_map = {
        'upload_image': [AllowAny],
        'list': [AllowAny],
        'retrieve': [AllowAny],
    }
    filterset_fields = ['status']
    # def get_queryset(self):
    #     super().get_queryset()
    
    @action(detail=False, methods=['POST'])
    def upload_image(self, request, *args):
        return Response(data=None, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['GET'])
    def get_project_owner(self, request, *args):
        owner = self.request.user
        queryset = Project.objects.filter(user=owner)
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
