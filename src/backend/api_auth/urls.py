from django.urls import path

from api_auth.views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

app_name = "api_auth"
urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
]
