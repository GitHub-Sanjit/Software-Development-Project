from django.shortcuts import render
from .forms import ExampleForm

# Create your views here.


def home(request):
    return render(request, "./first_app/home.html")


def about(request):
    return render(request, "./first_app/about.html")


def Example_form(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = ExampleForm()
    return render(request, "./first_app/django_form.html", {"form": form})
