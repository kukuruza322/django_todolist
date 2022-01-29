from django.shortcuts import render
from django.http import HttpResponse  # we can delete this because of using of class-based view representation
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Task


class TaskList(ListView):
    model = Task                   # model = Task because of this is the name of the class (form) in models.py, and that's refers on all objects of it !
    context_object_name = 'tasks'  # changing the name of object for HTML templates to 'tasks' and 'task'


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html' # allows to change task_detail to task.html


class TaskCreate(CreateView):
    model = Task
    fields = '__all__'   # get list of all attributes of class Task or all Models values,
                        # can be replaced by ['title', 'description', 'complete', 'created']
    success_url = reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')