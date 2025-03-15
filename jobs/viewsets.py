from rest_framework import viewsets
from jobs.models import Jobs
from jobs.permissions import IsSuperuserOrRecruiter
from jobs.serializers import JobsSerializer
from rest_framework import permissions

class JobViewSet(viewsets.ModelViewSet):
    serializer_class = JobsSerializer
    queryset = Jobs.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated, IsSuperuserOrRecruiter]
        
        return [permission() for permission in permission_classes]
