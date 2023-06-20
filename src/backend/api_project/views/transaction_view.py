from api_base.views import BaseViewSet
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
    
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     # update fund_total and fund_used project
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    # def all_transactions_project