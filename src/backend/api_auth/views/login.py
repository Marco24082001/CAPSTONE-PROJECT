from rest_framework_simplejwt.views import TokenObtainPairView
from api_auth.serializers import MyTokenObtainPairSerializer
from api_base.views import BaseViewSet

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
