from django.db import models
from category.models import CategoryModel

# Create your models here.


class TaskModel(models.Model):
    task_title = models.CharField(max_length=250)
    task_description = models.TextField()
    is_completed = models.BooleanField(default=False)
    task_assign = models.DateTimeField(auto_now_add=True)
    task_categories = models.ManyToManyField(CategoryModel)

    def __str__(self):
        return self.task_title
