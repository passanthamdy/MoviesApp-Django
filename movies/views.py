from django.shortcuts import render

from movies.serializer import MovieSerializer
from .models import Movie
from django.shortcuts import redirect
from django.urls import reverse
from .forms import MovieForm
from rest_framework import generics
# Create your views here.
def index(request):
    movies=Movie.objects.all()
    mov=Movie.objects.get(id=1)
    context={
        'movies':movies,
    }
    g=mov.actors.all()
    print(g[0])
    return render(request, 'movies/index.html',context)

def movie_details(request,id):
    movie=Movie.objects.get(id=id)
    context={
        'movie':movie,
    }
    print(movie.actors)
    return render(request,'movies/movie_details.html',context)

def create_movie(request):
    if request.method == "POST":
        form = MovieForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            return redirect(reverse('movies:movie_details', kwargs={'id' :movie.id}))

    else:
        form = MovieForm()
    return render(request, 'movies/create_movie.html', {'form': form})


def update_movie(request,id):
    movie=Movie.objects.get(id=id)
    
    if request.method == "POST":
        form = MovieForm(data=request.POST, files=request.FILES, instance=movie)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            return redirect(reverse('movies:movie_details', kwargs={'id' :movie.id}))

    else:
        form = MovieForm(instance=movie)  
    
    return render(request, 'movies/movie_update.html', {'form': form,'movie' :movie})

def delete_movie(request,id):
    movie=Movie.objects.get(id=id)
    movie.delete()
    return redirect(reverse('movies:list-movies'))

"""
Api version using generics in restframework
"""
class ListCreateMovie(generics.ListCreateAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer

class RetrieveUpdateestroyMovie(generics.RetrieveUpdateDestroyAPIView):
        queryset=Movie.objects.all()
        serializer_class=MovieSerializer