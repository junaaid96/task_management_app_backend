from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import F
from task_management_app_backend.constants import STATUS

User = get_user_model()


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    deadline = models.DateTimeField()
    position = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tasks')

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.title


class Subtask(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent_task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='subtasks')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='subtasks')

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)

        if is_new:
            Task.objects.filter(pk=self.parent_task.pk).update(
                position=F('position') + 1)

    def __str__(self):
        return f"{self.parent_task.title} - {self.title} - {self.status}"
