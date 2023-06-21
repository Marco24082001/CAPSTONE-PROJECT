from rest_framework.routers import DefaultRouter
from api_project.views import TypeViewSet, TransactionViewSet, ProjectViewSet, ReportViewSet

app_name = "api_project"
router = DefaultRouter()
router.register(r"types", TypeViewSet, basename=app_name)
router.register(r"transactions", TransactionViewSet)
router.register(r"projects", ProjectViewSet)
router.register(r"reports", ReportViewSet)
urlpatterns = router.urls
