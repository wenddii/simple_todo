from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .models import Task
from .forms import TaskForm,RegisterForm


# Login
def login_view(request):
    if request.user.is_authenticated:
        return redirect('list')

    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        return redirect('list')

    return render(request, "registration/login.html", {"form": form})


# Logout
def logout_view(request):
    logout(request)
    return redirect('login')


# Task list + create
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)

    form = TaskForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        return redirect('list')

    return render(request, 'tasks/list.html', {
        'tasks': tasks,
        'form': form
    })

@login_required
def updateTask(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    form = TaskForm(request.POST or None, instance=task)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('list')
    return render(request, 'tasks/update.html', {'form': form})


@login_required
def deleteTask(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('list')
    return render(request, 'tasks/delete.html', {'item': task})


def register_view(request):
    if request.user.is_authenticated:
        return redirect('list')

    form = RegisterForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)  # auto login after signup
        return redirect('list')

    return render(request, "registration/register.html", {"form": form})