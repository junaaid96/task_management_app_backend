from django.db import models
from django.contrib.auth.models import AbstractUser
from task_management_app_backend.constants import ROLES


class User(AbstractUser):
    role = models.CharField(max_length=10, choices=ROLES, default='user')
