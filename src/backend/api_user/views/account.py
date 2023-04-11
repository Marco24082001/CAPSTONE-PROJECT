from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from api_user.models import Account
from api_user.serializers import AccountSerializer

class ListCreateAccountView(ListCreateAPIView):
    model = Account
    serializer_class = AccountSerializer

    def get_queryset(self):
        return Account.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = AccountSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Create a new Car successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Car unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

class UpdateDeleteAccountView(RetrieveUpdateDestroyAPIView):
    model = Account
    serializer_class = AccountSerializer

    def put(self, request, *args, **kwargs):
        account = get_object_or_404(Account, id=kwargs.get('pk'))
        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Update Car successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Car unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        account = get_object_or_404(Account, id=kwargs.get('pk'))
        account.delete()
        return JsonResponse({
            'message': 'Delete Car successful!'
        }, status=status.HTTP_200_OK)
