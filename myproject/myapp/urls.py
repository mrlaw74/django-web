from django.urls import path
from .views import home, edit_task, delete_task, dashboard
from . import views
from .views import TaskListCreateView, TaskDetailView

urlpatterns = [
    path('', home, name='home'),
    path('edit/<int:task_id>/', edit_task, name='edit_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('api/tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('api/tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]
