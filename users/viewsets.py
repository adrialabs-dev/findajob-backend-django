from rest_framework import permissions
from rest_framework import viewsets
from users.permissions import IsSuperuser
from users.models import User
from users.serializers import UserRegisterSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated, IsSuperuser]
        
        return [permission() for permission in permission_classes]