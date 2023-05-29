from api_base.views import BaseViewSet
from api_project.models import Transaction
from api_project.serializers import TransactionSerializer

class TransactionViewSet(BaseViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
