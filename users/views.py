from rest_framework import generics, permissions
from users.models import User
from users.serializers import UserDetailSerializer
from jobs.permissions import IsSuperuserOrRecruiter


class UserCreateView(generics.CreateAPIView):
    # queryset = User.objects.all()
    # serializer_class = UserDetailSerializer
    permission_classes = [permissions.AllowAny]
    allowed_methods = ["POST"]


class UserListView(generics.ListAPIView):
    allowed_methods = ["GET"]
    # queryset = User.objects.all()
    # serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperuserOrRecruiter]


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperuserOrRecruiter]
