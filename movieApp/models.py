from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timesince import timesince

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

class User(AbstractUser):
    display_name = models.CharField(max_length=150, blank=True)
    mobilenumber = models.CharField(null=True, max_length=15)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

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
    liked_by = models.ManyToManyField(User, related_name="liked_movies", blank=True)

    @property
    def runtime_hm(self):
        hours = self.runtime // 60
        minutes = self.runtime % 60
        return f"{hours}h {minutes}m"

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist")
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'movie']
    @property
    def time_added(self):
        return timesince(self.added_at)
    

    
    
    

