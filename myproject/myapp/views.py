from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def home(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():  # Validate form data
            form.save()  # Save to the database
            return redirect('home')  # Redirect to home page

    return render(request, 'home.html', {'tasks': tasks, 'form': form})
