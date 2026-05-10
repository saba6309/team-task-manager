from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SignupForm, ProjectForm, TaskForm
from .models import Project, Task, Profile
from datetime import date
from django.http import HttpResponse


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()

            Profile.objects.create(user=user, role='Member')

            return redirect('login')

    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'login.html')


@login_required
def dashboard(request):

    filter_type = request.GET.get('filter')

    tasks = Task.objects.all()

    if filter_type == 'completed':
        tasks = tasks.filter(status='Completed')

    elif filter_type == 'pending':
        tasks = tasks.filter(status='Pending')

    elif filter_type == 'overdue':
        tasks = tasks.filter(
            due_date__lt=date.today()
        ).exclude(status='Completed')

    total = Task.objects.count()

    completed = Task.objects.filter(
        status='Completed'
    ).count()

    pending = Task.objects.filter(
        status='Pending'
    ).count()

    overdue = Task.objects.filter(
        due_date__lt=date.today()
    ).exclude(status='Completed').count()

    return render(request, 'dashboard.html', {
        'tasks': tasks,
        'total': total,
        'completed': completed,
        'pending': pending,
        'overdue': overdue
    })


@login_required
def create_project(request):

    profile, created = Profile.objects.get_or_create(user=request.user)

    if profile.role != 'Admin':
        return HttpResponse("Only Admin can create projects")

    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()

            return redirect('dashboard')

    else:
        form = ProjectForm()

    return render(request, 'project.html', {'form': form})

@login_required
def create_task(request):

    profile, created = Profile.objects.get_or_create(user=request.user)

    if profile.role != 'Admin':
        return HttpResponse("Only Admin can create tasks")

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = TaskForm()

    return render(request, 'task.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def delete_task(request, task_id):

    profile, created = Profile.objects.get_or_create(user=request.user)

    if profile.role != 'Admin':
        return HttpResponse("Only Admin can delete tasks")

    task = Task.objects.get(id=task_id)

    task.delete()

    return redirect('dashboard')

from django.shortcuts import redirect, get_object_or_404
from .models import Task

def update_status(request, task_id, status):
    task = get_object_or_404(Task, id=task_id)

    task.status = status
    task.save()

    return redirect('dashboard')