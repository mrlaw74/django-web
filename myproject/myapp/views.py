from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Task
from .forms import TaskForm
from django.http import HttpResponseRedirect
from django.urls import reverse

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer

from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto login after registration
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user).order_by('-priority', 'due_date')
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Assign the task to the logged-in user
            task.save()
            return redirect('home')

    return render(request, 'home.html', {'tasks': tasks, 'form': form})

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if task.user != request.user:
        return HttpResponseForbidden("You are not allowed to edit this task.")

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            print("✅ Task updated successfully!")  # Debugging
            return HttpResponseRedirect(reverse('home'))  # Redirect to home
        else:
            print("❌ Form is invalid:", form.errors)  # Debugging

    form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form, 'task': task})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    # Prevent deleting someone else's task
    if task.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this task.")

    task.delete()
    return redirect('home')

@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)

    # Filtering logic
    priority = request.GET.get('priority')
    status = request.GET.get('status')
    due_date = request.GET.get('due_date')

    if priority:
        tasks = tasks.filter(priority=priority)

    if status == 'completed':
        tasks = tasks.filter(completed=True)
    elif status == 'pending':
        tasks = tasks.filter(completed=False)

    if due_date:
        tasks = tasks.filter(due_date=due_date)

    return render(request, 'dashboard.html', {'tasks': tasks})