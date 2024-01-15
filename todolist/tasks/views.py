from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import add_taskForm, TaskForm
from .models import Task
from django.contrib.auth import get_user_model
from django.contrib import messages
from django import forms
from datetime import date


# Create your views here.
@login_required
def home(request):
    form = add_taskForm()
    MyDay_tasks = Task.objects.filter(created_at=date.today(),UserID=request.user)
    search_query = request.GET.get('search', '')
    if search_query:
        user_tasks = Task.objects.filter(UserID=request.user, TName__icontains=search_query)
    else:
        user_tasks = "nothing"
    if request.method == 'POST':
        form = add_taskForm(request.POST)
        if form.is_valid():
            # Process the form data, e.g., save the task to the database
            form.save()
            return render(request, 'tasks/add_task.html')
        else:
            print(form.errors)

    return render(request, 'tasks/home.html', {'form': form, 'MyDay_tasks': MyDay_tasks,'user_tasks': user_tasks, 'search_query': search_query})

@login_required
def important(request):
    form = add_taskForm()
    important_tasks = Task.objects.filter(Priority="High",UserID=request.user)
    search_query = request.GET.get('search', '')
    if search_query:
        user_tasks = Task.objects.filter(UserID=request.user, TName__icontains=search_query)
    else:
        user_tasks = "nothing"
    if request.method == 'POST':
        form = add_taskForm(request.POST)
        if form.is_valid():
            # Process the form data, e.g., save the task to the database
            form.save()
            return render(request, 'tasks/add_task.html')
        else:
            print(form.errors)

    return render(request, 'tasks/important.html', {'form': form, 'important_tasks': important_tasks,'user_tasks': user_tasks, 'search_query': search_query})

@login_required
def all_tasks(request):
    form = add_taskForm()
    all_tasks = Task.objects.filter(UserID=request.user)
    search_query = request.GET.get('search', '')
    if search_query:
        user_tasks = Task.objects.filter(UserID=request.user, TName__icontains=search_query)
    else:
        user_tasks = "nothing"
    if request.method == 'POST':
        form = add_taskForm(request.POST)
        if form.is_valid():
            # Process the form data, e.g., save the task to the database
            form.save()
            return render(request, 'tasks/add_task.html')
        else:
            print(form.errors)

    return render(request, 'tasks/all_tasks.html', {'form': form, 'all_tasks': all_tasks,'user_tasks': user_tasks, 'search_query': search_query})


@login_required
def add_task(request):
    User = get_user_model()
    if request.method == 'POST':
        form = add_taskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            if isinstance(request.user, User):
                task.UserID = request.user
            else:
                # If user is wrapped in SimpleLazyObject, unwrap it
                user_instance = User.objects.get(pk=request.user.pk)
                task.UserID = user_instance
            task.save()
            return redirect('home')
    return render(request, 'tasks/add_task.html', {'form': add_taskForm()})

def delete_task(request, pk):
    # Retrieve the task instance
    task = get_object_or_404(Task, TaskID=pk)
    task.delete()
    return redirect('all_tasks')


def edit_task(request, pk):
    # Retrieve the task instance
    task = get_object_or_404(Task, TaskID=pk)

    # Check if the task belongs to the current user to prevent unauthorized editing
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('all_tasks')  # Redirect to the task list page
    else:
        form = TaskForm(instance=task)

    # Redirect back to the same page (you might want to redirect to a different page)
    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})
'''
@login_required
def search_bar(request):
    search_query = request.GET.get('search', '')  # Get the search query from the request
    user_tasks = Task.objects.filter(UserID=request.user, TName__icontains=search_query)
    print(f"Search Query: {search_query}")
    print(f"User Tasks: {user_tasks}")
    return render(request, 'tasks/home.html', {'user_tasks': user_tasks, 'search_query': search_query})
'''

'''
def search_bar_page(request):
    search_query = request.GET.get('search', '')
    if search_query:
        user_tasks = Task.objects.filter(UserID=request.user, TName__icontains=search_query)
    else:
        user_tasks = Task.objects.filter(UserID=request.user)
    if request.method == 'POST':
        form = add_taskForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'tasks/add_task.html')

    return render(request, 'tasks/all_tasks.html', {'form': form, 'user_tasks': user_tasks, 'search_query': search_query})
'''