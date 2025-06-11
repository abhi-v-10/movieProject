from movieApp.models import *

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *




@api_view(['POST'])
def post_movie_api(request):
    data = request.data
    name = data['name']
    language = data['language']
    rel_year = data['rel_year']
    genre = data['genre']
    hero = data['hero']
    heroine = data['heroine']
    imdb_rating = data['imdb_rating']
    runtime = data['runtime']

    serializer = MovieSerializer(data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message" : "Sucess"})
    else:
        return Response(serializer.errors)

@api_view(['GET'])
def get_movie_api(request):
    movie = Movies.objects.all()
    serializer = MovieSerializer(movie, many=True)
    
    return Response({
        'data':serializer.data
    })

def update_movie_api(request, id):
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

    context = {"movie":movie}
    return render(request, 'update_movies.html', context)


def delete_movie_api(request, id):
    movie = Movies.objects.get(id=id)
    movie.delete()
    return redirect('get_movie')


