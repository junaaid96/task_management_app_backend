from django.contrib import admin
from .models import Task, Subtask


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status',
                    'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('status', 'created_at', 'updated_at')


class SubtaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status',
                    'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('status', 'created_at', 'updated_at')


admin.site.register(Task, TaskAdmin)
admin.site.register(Subtask, SubtaskAdmin)
