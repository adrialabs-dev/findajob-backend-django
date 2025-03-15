from rest_framework import generics, permissions
from users.models import User
from users.serializers import UserRegisterSerializer
from jobs.permissions import IsSuperuserOrRecruiter

class UserListView(generics.ListAPIView):
    allowed_methods = ["GET", "POST"]
class UserDetailView(generics.RetrieveAPIView):
    allowed_methods = ["GET", "PUT", "PATCH" "DELETE"]
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperuserOrRecruiter]
