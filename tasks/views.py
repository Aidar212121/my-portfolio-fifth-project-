from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from django.core.paginator import Paginator
Paginator


from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Главная страница")

def view_task(request, task_id):
    return HttpResponse(f"Просмотр задачи {task_id}")

def create_task(request):
    return HttpResponse("Создание задачи")

def edit_task(request, task_id):
    return HttpResponse(f"Редактирование задачи {task_id}")

def delete_task(request, task_id):
    return HttpResponse(f"Удаление задачи {task_id}")

def task_list(request):
    return render(request, 'tasks/task_list.html')

def task_create(request):
    return render(request, 'tasks/task_create.html')

def task_edit(request, id):
    return render(request, 'tasks/task_edit.html', {
        'id': id
    })

def task_delete(request, id):
    return render(request, 'tasks/task_delete.html', {
        'id': id
    })

def index(request):
    task=Task.objects.all()
    return render(request,'taskss/index.html',{'tasks':task})
def view_task(request):
    task=get_object_or_404(Task,pk=task_id)
    return render(request,'tasks/view_task.html',{"tasks":task})

def create_task(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST.get('description','')
        Task.objects.create(title=title, description=description)
        return redirect('index')
    return render(request, 'tasks/create_task.html')

def edit_task(request):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST.get('description','')
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('index')
    return render(request, 'tasks/edit_task.html',{"task": task})

def task_complete(request, id):
    task = get_object_or_404(Task, id=id)
    task.complete=True
    task.save()
    return redirect('task_list')

def task_list(request):
    tasks=Task.objects.all().order_by('-created')
    return render(request,'tasks/task_index.html',{'tasks':tasks})

def task_list(request):
    tasks = Task.objects.all()

    paginator = Paginator(tasks,5)
    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(request,'tasks/task_list.html',{'page_obj': page_obj})

