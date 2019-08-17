from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

from .models import Project


class ProjectView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        return Response({"projects": projects})
