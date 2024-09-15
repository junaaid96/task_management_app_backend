from rest_framework import viewsets, permissions
from .models import Task, Subtask
from .serializers import TaskSerializer, SubtaskSerializer
from task_management_app_backend.permissions import IsAdmin, IsUser


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdmin]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]


class SubtaskViewSet(viewsets.ModelViewSet):
    queryset = Subtask.objects.all()
    serializer_class = SubtaskSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdmin]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]
