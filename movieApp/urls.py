from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,

)



urlpatterns = [
    
    path('', views.home, name="home"),
    
    path('post_movie/', views.post_movie, name="post_movie"),
    path('get_movie/', views.get_movie, name="get_movie"),
    path('update_movie/<int:id>', views.update_movie, name="update_movie"),
    path('delete_movie/<int:id>', views.delete_movie, name="delete_movie"),
    path('add_relations/', views.add_relations, name="add_relations"),
    path('like/<int:movie_id>/', views.like_movie, name='like_movie'),
    path('watchlist/', views.watchlist, name='watchlist'),

    
    path('create_user/', views.create_user, name="create_user"),
    path('login_user/', views.login_user, name="login_user"),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('edit_user/', views.edit_user, name='edit_user'),
    path('profile/', views.profile, name='profile'),
    path('add_user/', views.add_user, name='add_user'),

    path("api_post_movie/", views.api_post_movie, name="api_post"),
    path("api_get_movie/", views.api_get_movie, name="api_get_movie"),
    path("api_update_movie/<int:id>", views.api_update_movie, name="api_update_movie"),
    path("api_delete_movie/<int:id>", views.api_delete_movie, name="api_delete_movie"),
    path("api_create_user/", views.api_create_user, name="api_create_user"),
    path("api_register/", views.api_register, name="api_register"),
    path("api_view_token/", views.api_view_token, name="api_view_token"),
    path("api_test_token/", views.api_test_token, name="api_test_token"),
    path("api_logout/", views.api_logout, name="api_logout"),

    path("create_token/", TokenObtainPairView.as_view(), name="create_token"),
    path("refresh_token/", TokenRefreshView.as_view(), name="refresh_token"),

    path("refresh_custom_token/", views.CustomPairView.as_view()),


]