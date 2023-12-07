from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.


def musician(request):
    if request.method == "POST":
        form = forms.MusicianForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("home")
    else:
        form = forms.MusicianForm()
    return render(request, "musician.html", {"form": form})


def edit_musician(request, id):
    musician = models.Musician.objects.get(pk=id)
    form = forms.MusicianForm(instance=musician)
    if request.method == "POST":
        form = forms.MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("home")
    return render(request, "musician.html", {"form": form})
