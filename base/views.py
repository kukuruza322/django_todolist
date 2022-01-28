from django.shortcuts import render
from django.http import HttpResponse  # we can delete this because of using of class-based view representation
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'  # changing the name of object for HTML templates to 'tasks' and 'task'


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html' # allows to change task_detail to task.html