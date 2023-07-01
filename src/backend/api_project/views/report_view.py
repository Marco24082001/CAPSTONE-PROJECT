from api_base.views import BaseViewSet
from api_base.exceptions import DataNotMatchHash
from api_project.models import Report
from api_project.serializers import ReportSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class ReportViewSet(BaseViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_map = {
        'list': [AllowAny],
        'retrieve': [AllowAny],
        'create': [AllowAny]
    }
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['created_at']
    ordering = ['created_at']
    filterset_fields = ['project']

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
