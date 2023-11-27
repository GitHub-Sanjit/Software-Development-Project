from django.shortcuts import render
import datetime

# Create your views here.


def home(request):
    d = {
        "author": "Rahim",
        "age": 5,
        "lst": ["python", "is", "best"],
        'birthDay':datetime.datetime.now(),
        'val':'',
        "courses": [
            {
                "id": 1,
                "name": "Python",
                "fee": 5000,
            },
            {
                "id": 2,
                "name": "Django",
                "fee": 6000,
            },
            {
                "id": 3,
                "name": "Typescript",
                "fee": 10000,
            },
        ],
    }
    return render(request, "home.html", d)
