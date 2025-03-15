from rest_framework import permissions
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from jobs.models import Jobs
from jobs.serializers import JobsSerializer
from jobs.permissions import IsSuperuserOrRecruiter

# class CreateJobsView(CreateAPIView):
#     allowef_methods = ["POST"]
#     permission_classes = [permissions.IsAuthenticated, IsSuperuserOrRecruiter]

class JobsListView(ListAPIView, CreateAPIView):
    allowed_methods = ["GET", "POST"]
    # permission_classes = [permissions.IsAuthenticated]

class JobsDetailView(RetrieveAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperuserOrRecruiter]