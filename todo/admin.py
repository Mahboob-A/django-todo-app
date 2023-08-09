from django.contrib import admin

# Register your models here.
from .models import Task 

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin): 
        list_display = ('id', 'task_name', 'is_completed', 'created_at', 'updated_at')
        search_fields = ('task_name', 'is_completed',)