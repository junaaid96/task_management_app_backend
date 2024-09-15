from rest_framework import viewsets
from .models import Task, Subtask
from .serializers import TaskSerializer, SubtaskSerializer
from task_management_app_backend.permissions import IsAdmin


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAdmin]


class SubtaskViewSet(viewsets.ModelViewSet):
    queryset = Subtask.objects.all()
    serializer_class = SubtaskSerializer
    permission_classes = [IsAdmin]
