from django.db import models
from django.contrib.auth.models import AbstractUser

# One-to-One relationship with MovieDetails
class MovieDetails(models.Model):
    budget = models.IntegerField()
    collection = models.IntegerField()

# ForeignKey (One-to-Many) relationship with Production
class Production(models.Model):
    name = models.CharField(max_length=100)
    

# Many-to-Many relationship with OtherLanguages
class OtherLanguages(models.Model):
    other_language = models.CharField(max_length=100)
    
class Movies(models.Model):
    name = models.CharField(max_length = 250)
    language = models.CharField(max_length = 100)
    rel_year = models.IntegerField()
    genre = models.CharField(max_length = 100)
    hero = models.CharField(max_length = 100)
    heroine = models.CharField(max_length = 100)
    imdb_rating = models.FloatField()
    runtime = models.IntegerField(help_text="Enter runtime in minutes")
    movie_details = models.OneToOneField(MovieDetails, null=True, on_delete=models.CASCADE)
    production = models.ForeignKey(Production, null=True, on_delete=models.CASCADE)
    other_languages = models.ManyToManyField(OtherLanguages, blank=True)



class User(AbstractUser):
    mobilenumber = models.CharField(null=True, max_length=15)
    age = models.IntegerField(null=True) 
    

    
    
    

