from rest_framework import permissions
from rest_framework import viewsets
from users.permissions import IsSuperuser
from users.models import User
from users.serializers import UserRegisterSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()
    # permission_classes = [permissions.IsAuthenticated, IsSuperuser]
