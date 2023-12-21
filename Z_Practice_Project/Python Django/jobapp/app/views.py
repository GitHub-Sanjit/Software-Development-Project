from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template import loader

# Create your views here.

job_title = [
    "first Job",
    "Second Job",
    "Third Job",
    "Fourth Job",
]

job_description = [
    "First Job Description",
    "Second Job Description",
    "Third Job Description",
    "Fourth Job Description",
]


# def hello(request):
#     return HttpResponse("<h3>Hello World!</h3>")

class TempClass:
    x = 5


def hello(request):
    list = ["alpha", "beta"]
    temp = TempClass()
    is_authenticated = False
    context = {"name": "Django", "age": 10,
               "first_list": list, "temp_object": temp, "is_authenticated": is_authenticated}
    return render(request, "app/hello.html", context)


def job_list(request):
    # list_of_jobs = "<ul>"
    # for j in job_title:
    #     job_id = job_title.index(j)
    #     detail_url = reverse('jobs_detail', args=(job_id,))
    #     list_of_jobs += f"<li><a href='{detail_url}'> {j}</a></li>"
    # list_of_jobs += "</ul>"
    # return HttpResponse(list_of_jobs)
    context = {"job_title_list": job_title}
    return render(request, "app/index.html", context)


def job_detail(request, id):
    print(type(id))

    try:
        if id == 0:
            return redirect(reverse("jobs_home"))
        context = {"job_title": job_title[id],
                   "job_description": job_description[id]}
        return render(request, "app/job_detail.html", context)
    except:
        return HttpResponseNotFound("Not Found")
