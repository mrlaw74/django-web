# Task Manager API

This API allows users to manage tasks, including authentication, task creation, retrieval, updating, and deletion.

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- Django
- Django REST Framework (DRF)
- Django Simple JWT

### Installation
```bash
# Clone the repository
git clone https://github.com/your-repo/task-manager-api.git
cd task-manager-api

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Start the development server
python manage.py runserver
```

## 🔑 Authentication

### Obtain Access & Refresh Tokens
```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "your_username", "password": "your_password"}'
```
_Response:_
```json
{
  "access": "your_access_token",
  "refresh": "your_refresh_token"
}
```

### Refresh Access Token
```bash
curl -X POST http://127.0.0.1:8000/api/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh": "your_refresh_token"}'
```

## 📌 API Endpoints

### 1️⃣ List & Create Tasks
**GET /api/tasks/** - Retrieve all tasks (requires authentication)
```bash
curl -X GET http://127.0.0.1:8000/api/tasks/ \
  -H "Authorization: Bearer your_access_token"
```

**POST /api/tasks/** - Create a new task
```bash
curl -X POST http://127.0.0.1:8000/api/tasks/ \
  -H "Authorization: Bearer your_access_token" \
  -H "Content-Type: application/json" \
  -d '{"title": "New Task", "priority": "High"}'
```

### 2️⃣ Retrieve, Update & Delete a Task
**GET /api/tasks/{id}/** - Retrieve task details
```bash
curl -X GET http://127.0.0.1:8000/api/tasks/1/ \
  -H "Authorization: Bearer your_access_token"
```

**PUT /api/tasks/{id}/** - Update a task
```bash
curl -X PUT http://127.0.0.1:8000/api/tasks/1/ \
  -H "Authorization: Bearer your_access_token" \
  -H "Content-Type: application/json" \
  -d '{"title": "Updated Task", "priority": "Medium"}'
```

**DELETE /api/tasks/{id}/** - Delete a task
```bash
curl -X DELETE http://127.0.0.1:8000/api/tasks/1/ \
  -H "Authorization: Bearer your_access_token"
```


# Task Manager API

## Overview
This project provides a Django-based task management system with both web and API functionality. Users can create, edit, and delete tasks, as well as authenticate using JWT.

## Web Endpoints
| Endpoint       | Description         |
|---------------|---------------------|
| `/`           | Home Page (Tasks)   |
| `/edit/<id>/` | Edit Task           |
| `/delete/<id>/` | Delete Task       |
| `/dashboard/` | Task Dashboard      |
| `/register/`  | User Registration   |
| `/login/`     | User Login          |
| `/logout/`    | User Logout         |

## URL Patterns in `myapp/urls.py`
```python
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
```

## Next Steps
- ✅ Implement pagination for large task lists.
- ✅ Improve UI with sorting and filtering options.
- ✅ Enhance security with user roles.
- ✅ Extend API with task categories and labels.

🚀 Happy Coding!

