from django.db import models
from musician.models import Musician

# Create your models here.


class Album(models.Model):
    album_name = models.CharField(max_length=225)
    musicians = models.ForeignKey(Musician, on_delete=models.CASCADE, default=25)
    release_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    def __str__(self):
        return self.album_name
