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
        'upload_image': [AllowAny]
    }
    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     print('page')
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         try:
    #             return self.get_paginated_response(serializer.data)
    #         except:
    #             print('loi')
    #     serializer = self.get_serializer(queryset, many=True)
    #     try:
    #         return Response(serializer.data)
    #     except:
    #         print('loi1')
    #         return Response({"thanh vi": "sfsfdsdf"}, status=status.HTTP_200_OK)
    @action(detail=False, methods=['POST'])
    def upload_image(self, request, *args):
        return Response(data=None, status=status.HTTP_200_OK)
