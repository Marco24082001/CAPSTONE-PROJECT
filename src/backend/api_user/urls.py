# from rest_framework_extensions.routers import DefaultRouter

from api_user.views import *

app_name = "api_user"
# router = DefaultRouter()

from django.urls import path
urlpatterns = [
    path('accounts', ListCreateAccountView.as_view()),
    path('accounts/<str:pk>', UpdateDeleteAccountView.as_view()),
]
