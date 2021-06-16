from django.db import models

# Create your models here.


class Movies(models.Model):
    title = models.CharField(max_length=20)
    keywords = models.CharField(max_length=100)
    cast = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    director = models.CharField(max_length=15)

    def __str__(self):
        return self.title
