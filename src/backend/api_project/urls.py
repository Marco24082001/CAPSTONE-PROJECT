from rest_framework.routers import DefaultRouter
# viewset
from api_project.views import TypeViewSet, TransactionViewSet, ProjectViewSet

app_name = "api_project"
router = DefaultRouter()
router.register(r"types", TypeViewSet, basename=app_name)
router.register(r"transactions", TransactionViewSet)
router.register(r"projects", ProjectViewSet)
urlpatterns = router.urls
