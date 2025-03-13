from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = models.CharField(max_length=150, null=True, blank=True)  
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=50, default='user')
    experience_level = models.CharField(max_length=100, default='junior')
    skills = models.JSONField(default=list, blank=True)
    years_of_experience = models.IntegerField(default=0)

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = [] 

    objects = UserManager()

    def __str__(self):
        return self.email