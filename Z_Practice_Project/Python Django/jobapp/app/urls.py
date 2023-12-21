
from django.urls import path

from . import views


urlpatterns = [
    path("", views.job_list, name="jobs_home"),
    path("hello/", views.hello, name="hello"),
    path("job/<int:id>", views.job_detail, name="jobs_detail"),
    # path("job/<str:id>", views.job_detail),
]
