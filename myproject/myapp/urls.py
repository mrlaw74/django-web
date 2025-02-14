from django.urls import path
from .views import home, edit_task, delete_task

urlpatterns = [
    path('', home, name='home'),
    path('edit/<int:task_id>/', edit_task, name='edit_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
]
