from rest_framework import viewsets
from jobs.models import Jobs
from jobs.permissions import IsUser
from jobs.serializers import JobsSerializer
from rest_framework import permissions

class JobViewSet(viewsets.ModelViewSet):
    serializer_class = JobsSerializer
    queryset = Jobs.objects.all()
    permission_classes = [permissions.IsAuthenticated]
