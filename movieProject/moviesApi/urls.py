from django.urls import path
from . import views

urlpatterns = [
    path('post_movie_api/', views.post_movie_api, name="post_movie_api"),
    path('get_movie_api/', views.get_movie_api, name="get_movie_api"),
    path('update_movie_api/<int:id>', views.update_movie_api, name="update_movie_api"),
    path('delete_movie_api/<int:id>', views.delete_movie_api, name="delete_movie_api"),
]