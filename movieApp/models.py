from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    mobilenumber = models.IntegerField(null=True)
    age = models.IntegerField(null=True) 

class Movies(models.Model):
    name = models.CharField(max_length = 250)
    language = models.CharField(max_length = 100)
    rel_year = models.IntegerField()
    genre = models.CharField(max_length = 100)
    hero = models.CharField(max_length = 100)
    heroine = models.CharField(max_length = 100)
    imdb_rating = models.FloatField()
    runtime = models.IntegerField(help_text="Enter runtime in minutes")


