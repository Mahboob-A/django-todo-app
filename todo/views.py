from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Task

def home(request): 
        template_path = 'todo/home.html'
        pending_tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
        completed_tasks = Task.objects.filter(is_completed=True).order_by('-updated_at')
        context = {
                'pending_tasks' : pending_tasks, 
                'completed_tasks' : completed_tasks, 
        }
        
        return render(request, template_path, context)

def add_task(request): 
        task = request.POST['task']  # task key is the name of input :  <input type="text" name="task" class="form-control" placeholder="Add a task">  
        Task.objects.create(task_name=task)
        return redirect('home')

def mark_task_completed(request, id): 
        task = Task.objects.get(id=id)
        task.is_completed = True 
        task.save()
        return redirect('home')

def mark_task_undone(request, pk): 
        task = get_object_or_404(Task, pk=pk)
        task.is_completed = False
        task.save()
        return redirect('home')


def update_task(request, id): 
        task = get_object_or_404(Task, id=id)
        template_path = 'todo/update_task.html'
        if request.method == 'POST': 
                updated_task = request.POST['task']
                task.task_name = updated_task
                task.save()
                return redirect('home')
        else: 
                context = {
                        'task' : task, 
                }
                return render(request, template_path, context)


def delete_task(request, id): 
        Task.objects.get(id=id).delete()
        return redirect('home')
