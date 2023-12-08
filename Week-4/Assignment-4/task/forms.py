from django import forms
from . import models


class TaskForm(forms.ModelForm):
    class Meta:
        model = models.TaskModel
        fields = "__all__"
        widgets = {
            "task_assign": forms.TextInput(attrs={"type": "datetime-local"}),
        }
