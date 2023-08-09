from django.urls import path

from .views import home, add_task, mark_task_completed, mark_task_undone, update_task, delete_task

urlpatterns = [
        path('', home, name='home'),
        path('add-task/', add_task, name='add-task'),
        path('mark-task-completed/<int:id>/', mark_task_completed, name='mark-task-completed'),
        path('mark-task-undone/<int:pk>/', mark_task_undone, name='mark-task-undone'),
        path('update-task/<int:id>/', update_task, name='update-task'),
        path('delete-task/<int:id>/', delete_task, name='delete-task'),
]
