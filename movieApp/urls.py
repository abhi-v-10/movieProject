from django.urls import path
from . import views

urlpatterns = [

    # Movie App URLs
    path('', views.home, name="home"),
    
    path('post_movie/', views.post_movie, name="post_movie"),
    path('get_movie/', views.get_movie, name="get_movie"),
    path('update_movie/<int:id>', views.update_movie, name="update_movie"),
    path('delete_movie/<int:id>', views.delete_movie, name="delete_movie"),
    path('create_user/', views.create_user, name="create_user"),
    path('login_user/', views.login_user, name="login_user"),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('profile/', views.profile, name='profile'),

    path("api_post_movie/", views.api_post_movie, name="api_post"),
    path("api_get_movie/", views.api_get_movie, name="api_get_movie"),
    path("api_update_movie/<int:id>", views.api_update_movie, name="api_update_movie"),
    path("api_delete_movie/<int:id>", views.api_delete_movie, name="api_delete_movie"),


]