from api_auth.serializers import RegisterSerializer
from api_user.serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view
from drf_yasg.utils import swagger_auto_schema

from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

@swagger_auto_schema(method='POST', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'first_name': openapi.Schema(type=openapi.TYPE_STRING, default='auto'),
        'last_name': openapi.Schema(type=openapi.TYPE_STRING, default='user'),
        'email': openapi.Schema(type=openapi.TYPE_STRING, default='auto@gmail.com'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, default='', format='password'),
    })
)
@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def register_user(request):
    data = request.data
    print(data)
    serializer = RegisterSerializer(data=data)
    try:
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# # other decorators if required
# @permission_classes([])
# def user_create(request):
#     serializer = UserSerializer(data=request.POST)
#     if serializer.is_valid():
#         password = serializer.validated_data.get("password")
#         serializer.object.set_password(password)
#         serializer.save()
#         return Response({"message": "User Created"}, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer.errors)