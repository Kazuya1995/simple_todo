from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.http import HttpRequest

# タスク一覧表示

def task_list(request: HttpRequest):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'todo/task_list.html', {'tasks': tasks})

# タスク追加

def add_task(request: HttpRequest):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        if title:
            Task.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request, 'todo/add_task.html')

# タスク完了

def complete_task(request: HttpRequest, task_id: int):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')

# タスク削除

def delete_task(request: HttpRequest, task_id: int):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')
