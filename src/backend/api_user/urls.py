from rest_framework.routers import DefaultRouter

from api_user.views import UserViewSet

app_name = "api_user"
router = DefaultRouter()
router.register(r"", UserViewSet, basename="user")

urlpatterns = router.urls
