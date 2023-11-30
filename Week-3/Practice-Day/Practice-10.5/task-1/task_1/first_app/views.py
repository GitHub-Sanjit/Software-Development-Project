from django.shortcuts import render
import datetime

# Create your views here.


def home(request):
    data = {
        "author": "Snajit Sarkar",
        "age": 50,
        "address": "Jashore",
        "list": [
            1,
            5,
            10,
            15,
            20,
            25,
            30,
            35,
            40,
            45,
            50,
            55,
            60,
            65,
            70,
            75,
            80,
            85,
            90,
            95,
            100,
        ],
        "lst": ["Django", "is", "not", "Joke"],
        "string": "My Name is Sanjit",
        "date": datetime.datetime.now(),
        "time": datetime.datetime.now(),
        "blog_date": "5 December 2023",
        "comment_date": "08:00 on 1 July 2022",
        "empty": "I am empty string",
        "divisibleby": 27,
        "size": 345643545734,
        "name": "My Name is Sanjit Sarkar",
        "title": "mY First post",
        'new':'He is a WebDeveloper',
        "hello": "You are a slug",
        "number": "one",
        "dictsort": [
            {"name": "zed", "age": 19},
            {"name": "amy", "age": 22},
            {"name": "joe", "age": 31},
        ],
        "courses": [
            {"id": 1, "name": "Django", "fee": 4000},
            {"id": 2, "name": "Javascript", "fee": 1500},
            {"id": 3, "name": "Python", "fee": 3500},
        ],
    }
    return render(request, "home.html", data)
