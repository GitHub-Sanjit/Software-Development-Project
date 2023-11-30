from django.shortcuts import render

# Create your views here.


def home(request):
    d = {
        "author": "Rahim",
        "age": 20,
        "lst": [1, 2, 3, 4, 5],
        "courses": [
            {"id": 1, "name": "Python", "fee": 1000},
            {"id": 2, "name": "Django", "fee": 2000},
            {"id": 3, "name": "Javascript", "fee": 3000},
            {"id": 4, "name": "C++", "fee": 4000},
        ],
    }
    return render(request, "home.html", d)
