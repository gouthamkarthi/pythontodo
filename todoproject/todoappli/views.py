from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import TodoForm
from .models import Task

from django.views.generic import ListView

from django.views.generic.detail import DetailView

from django.views.generic.edit import UpdateView, DeleteView


# Create your views here.
# Class Based List View
# class Tasklistview(ListView):
#     model = Task
#     template_name = 'index.html'
#     context_object_name = 'end'
#
#
# # Class Based Detail View
#
# class TaskDetailView(DetailView):
#     model = Task
#     template_name = 'details.html'
#     context_object_name = 'end'
#
#
# # Class Based Update View
# class TaskUpdateView(UpdateView):
#     model = Task
#     template_name = 'edit.html'
#     context_object_name = 'form'
#     fields = ('task_name', 'task_priority', 'task_date')
#
#     def get_success_url(self):
#         return reverse_lazy('cbvdetail', kwargs={'pk': self.object.id})
#
#
# # Class Based Delete View
# class Taskdeleteview(DeleteView):
#     model = Task
#     template_name = 'delete.html'
#     success_url = reverse_lazy('cbvindex')

# ______________________________________
def index(request):
    task = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task-name', '')
        priority = request.POST.get('task-priority', '')
        date = request.POST.get('date', '')
        add_task = Task(task_name=name, task_priority=priority, task_date=date)
        add_task.save()
    return render(request, 'index.html', {'end': task})
#
# _____________________________________
# def details(request):
#
#     return render(request, 'details.html', {'end': task})
# ________________________________________________
def delete(request, taskid):
    task_delete = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task_delete.delete()
        return redirect('/')
    return render(request, 'delete.html')
#
# ______________________
def update(request, id):
    task = Task.objects.get(id=id)
    fan = TodoForm(request.POST or None, instance=task)
    if fan.is_valid():
        fan.save()
        return redirect('/')
    return render(request, 'edit.html', {'fan': fan, 'task': task})
