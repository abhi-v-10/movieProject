from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import *
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from .serializer import MovieSerializer
# from django.contrib.auth.models import User

# Movie App Views
def home(request):
    return render(request, 'home.html')

def post_movie(request):
    if request.method == "POST":
        name = request.POST.get('name')
        language = request.POST.get('language')
        rel_year = request.POST.get('rel_year')
        genre = request.POST.get('genre')
        hero = request.POST.get('hero')
        heroine = request.POST.get('heroine')
        rating = request.POST.get('rating')
        runtime = request.POST.get('runtime')
        movie = Movies.objects.create(name=name, language=language, rel_year=rel_year, genre=genre, hero=hero, heroine=heroine, imdb_rating=rating, runtime=runtime)
        return redirect('get_movie')
    return render(request, 'post_movies.html')

def get_movie(request):
    movie = Movies.objects.all()
    context = {"movie":movie}
    return render(request, 'get_movies.html', context)

def update_movie(request, id):
    try:
        movie = Movies.objects.get(id=id)
        if request.method == "POST":
            movie.name = request.POST.get("name")
            movie.language = request.POST.get("language")
            movie.rel_year = request.POST.get("rel_year")
            movie.genre = request.POST.get("genre")
            movie.hero = request.POST.get("hero")
            movie.heroine = request.POST.get("heroine")
            movie.imdb_rating = request.POST.get("rating")
            movie.runtime = request.POST.get("runtime")
            movie.save()
            return redirect('get_movie')
        else:
            context = {"movie":movie}
            return render(request, 'update_movies.html', context)
    except Movies.DoesNotExist:
        return HttpResponse("Movie not found", status=404)


def delete_movie(request, id):
    try:
        movie = Movies.objects.get(id=id)
        movie.delete()
        return redirect('get_movie')
    except Movies.DoesNotExist:
        return HttpResponse("Movie not found", status=404)

    
def create_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        mobilenumber = request.POST.get('mobilenumber')
        age = request.POST.get('age')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists", status=400)
        
        user = User.objects.create_user(username=username, password=password, mobilenumber=mobilenumber, age=age)
        user.save()
        return HttpResponse("User created successfully", status=201)
    else:
        return render(request, 'create_user.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return HttpResponse("Invalid credentials", status=401)
    return render(request, 'login_user.html')

@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})

def logout_user(request):
    logout(request)
    return redirect('login_user')


@api_view(['POST'])
def api_post_movie(request):
    data = request.data
    serializer = MovieSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "posted"}, status=201)
    return Response({"message": "failed"})


@api_view(['GET'])
def api_get_movie(request):
    movie = Movies.objects.all()
    serializer = MovieSerializer(movie, many=True)
    return Response({"movie": serializer.data})

@api_view(['PUT'])
def api_update_movie(request, id):
    try:
        movie = Movies.objects.get(id=id)
    except Movies.DoesNotExist:
        return Response({"message": "Movie not found"}, status=404)
    
    serializer = MovieSerializer(movie, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Movie updated successfully"})
    else:
        return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def api_delete_movie(request, id):
        try:
            movie = Movies.objects.get(id=id)
            movie.delete()
            return Response({"message": "Movie deleted successfully"})
        except Movies.DoesNotExist:
            return Response({"message": "Movie not found"}, status=404)




