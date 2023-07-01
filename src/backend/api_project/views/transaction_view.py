from api_base.views import BaseViewSet
from api_base.exceptions import DataNotMatchHash
from api_project.models import Transaction
from api_project.serializers import TransactionSerializer
from api_project.serializers import ProjectSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class TransactionViewSet(BaseViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_map = {
        'list': [AllowAny],
        'retrieve': [AllowAny],
        'create': [AllowAny]
    }
    filterset_fields = ['project', 'type_transaction']


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
