from django import forms
from .models import Task


class TodoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'task_priority', 'task_date']
