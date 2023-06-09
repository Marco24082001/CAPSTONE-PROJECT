from api_base.views import BaseViewSet
from api_project.models import Project
from api_project.serializers import ProjectSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny




class ProjectViewSet(BaseViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    serializer_map = {}
    permission_map = {
        'upload_image': [AllowAny],
        'list': [AllowAny],
        'retrieve': [AllowAny],
    }
    # def get_queryset(self):
    #     super().get_queryset()
    
    @action(detail=False, methods=['POST'])
    def upload_image(self, request, *args):
        return Response(data=None, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['GET'])
    def get_project_owner(self, request, *args):
        owner = self.request.user
        print(owner)
        queryset = Project.objects.filter(user=owner)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
