from api_base.views import BaseViewSet
from api_project.models import Project
from api_project.serializers import ProjectSerializer

class ProjectViewSet(BaseViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
