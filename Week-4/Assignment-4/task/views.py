from django.shortcuts import render, redirect
from . import models
from . import forms

# Create your views here.


def add_task(request):
    if request.method == "POST":
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = forms.TaskForm()
    return render(request, "add_task.html", {"form": form})


def edit_task(request, id):
    task = models.TaskModel.objects.get(pk=id)
    update_task = forms.TaskForm(instance=task)

    if request.method == "POST":
        form = forms.TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request, "add_task.html", {"form": update_task})


def delete_task(request, id):
    task = models.TaskModel.objects.get(pk=id)
    task.delete()
    return redirect("home")
