from rest_framework import permissions

class IsSuperuserOrRecruiter(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['superuser', 'recruiter']
    
class IsUser(permissions.BasePermission):
    def has_user_permission(self, request, view):
        return request.user.role in ['user']