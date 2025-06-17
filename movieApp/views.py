from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import status
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from .models import *
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .serializer import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from .forms import *
# from django.contrib.auth.models import User


class CustomPairView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer

# Movie App Views
def home(request):
    return render(request, 'home.html')

@permission_classes([IsAuthenticated])
def post_movie(request):
    if request.method == "POST":
        serializer = MovieSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('add_relations')
        else:
            return render(request, 'post_movies.html', {'errors': serializer.errors})
    return render(request, 'post_movies.html')

@permission_classes([AllowAny])
def get_movie(request):
    name = request.GET.get('name')
    language = request.GET.get('language')
    genre = request.GET.get('genre')
    rel_year = request.GET.get('rel_year')
    movie = Movies.objects.all()
    if name:
        movie = movie.filter(name__icontains=name)
    if language:
        movie = movie.filter(language__icontains=language)
    if genre:
        movie = movie.filter(genre__icontains=genre)
    if rel_year:
        movie = movie.filter(rel_year=rel_year)
    context = {"movie":movie}
    return render(request, 'get_movies.html', context)

@permission_classes([IsAuthenticated])
def update_movie(request, id):
    
    try:
        details = MovieDetails.objects.all()
        production = Production.objects.all()
        other_languages = OtherLanguages.objects.all()
        movie = Movies.objects.get(id=id)
        errors = {}

        if request.method == "POST":
            data = {
                "name": request.POST.get("name"),
                "language": request.POST.get("language"),
                "rel_year": request.POST.get("rel_year"),
                "genre": request.POST.get("genre"),
                "hero": request.POST.get("hero"),
                "heroine": request.POST.get("heroine"),
                "imdb_rating": request.POST.get("imdb_rating"),
                "runtime": request.POST.get("runtime"),
                "movie_details": request.POST.get("movie_details"),
                "production": request.POST.get("production"),
                "other_languages": request.POST.getlist("other_languages")
            }

            serializer = MovieSerializer(instance=movie, data=data)

            if serializer.is_valid():
                serializer.save()
                return redirect('get_movie')
            else:
                return render(request, 'update_movies.html', {
                    "movie": movie,
                    "details": details,
                    "productions": production,
                    "other_languages": other_languages,
                    "errors": serializer.errors,
                    "form_data": data
                })

        else:
            return render(request, 'update_movies.html',
             {
                "movie": movie, "details": details,
                "productions": production,
                "other_languages": other_languages
            })

    except Movies.DoesNotExist:
        return HttpResponse("Movie not found", status=404)


@permission_classes([IsAuthenticated])
def delete_movie(request, id):
    try:
        movie = Movies.objects.get(id=id)
        movie.delete()
        return redirect('get_movie')
    except Movies.DoesNotExist:
        return HttpResponse("Movie not found", status=404)

# User Authentication Views 

def create_user(request):
    if request.method == "POST":
        data = {
            "username": request.POST.get("username", ""),
            "password": request.POST.get("password", ""),
            "mobilenumber": request.POST.get("mobilenumber", ""),
            "age": request.POST.get("age", "")
        }

        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return redirect('login_user')
        else:
            return render(request, "create_user.html", {
                "errors": serializer.errors,
                "data": data
            })

    return render(request, "create_user.html", {
        "data": {}
    })
        

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



@permission_classes([IsAuthenticated])
def logout_user(request):
    logout(request)
    return redirect('login_user')

@permission_classes([IsAuthenticated])
def profile(request):
    return render(request, 'profile.html', {'user': request.user})

@permission_classes([IsAuthenticated])
def add_relations(request):
    if request.method == "POST":
        budget = request.POST.get('budget')
        collection = request.POST.get('collection')
        production_name = request.POST.get('production_name')
        other_languages_str = request.POST.get('other_languages')

        # Save MovieDetails
        if budget and collection:
            MovieDetails.objects.create(budget=budget, collection=collection)

        if production_name.strip():
            Production.objects.create(name=production_name)
        return redirect('get_movie')
    return render(request, 'relationships.html')

# ModelForm Views
def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})


# API Views

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

@api_view(['POST'])
def api_create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created successfully"}, status=201)


@api_view(['POST'])
@permission_classes([AllowAny])
def api_register(request):    
    serializer = UserSerializer(data=request.data)    
    serializer.is_valid(raise_exception=True)    
    serializer.save()    
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([AllowAny])
def api_view_token(request):
    serializer = TokenObtainPairSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
    except TokenError as e:
        raise InvalidToken(e.args[0])
    return Response(serializer.validated_data, status=200)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_test_token(request):
    return Response({"message": "Token is valid"}, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_logout(request):
    refresh_token = request.data.get('refresh_token')
    token = RefreshToken(refresh_token)
    token.blacklist()
    return Response({"message": "Logged out successfully"}, status=205)