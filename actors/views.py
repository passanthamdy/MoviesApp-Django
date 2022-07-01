from django.shortcuts import render
from actors.serializers import ActorSerializer
from .models import Actor
from .forms import ActorForm
from django.shortcuts import redirect
from django.urls import reverse
from movies.models import Movie
from rest_framework import generics
# Create your views here.
def home(request):
    actors=Actor.objects.all()
    context={
        'actors':actors,
    }
    return render(request, 'actors/index.html',context)

def actor_details(request,id):
    actor=Actor.objects.get(id=id)
    
    movies=Movie.objects.filter(actors__id=id)
    print(movies)
    context={
        'actor':actor,
    }
    return render(request,'actors/actor_details.html',context)

def actor_create(request):
    if request.method == "POST":
        form = ActorForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            actor = form.save(commit=False)
            actor.save()
            return redirect(reverse('actors:actor_details', kwargs={'id' :actor.id}))

    else:
        form = ActorForm()
    return render(request, 'actors/add_actor.html', {'form': form})

def actor_update(request,id):
    actor=Actor.objects.get(id=id)
    
    if request.method == "POST":
        form = ActorForm(data=request.POST, files=request.FILES, instance=actor)
        if form.is_valid():
            actor = form.save(commit=False)
            actor.save()
            return redirect(reverse('actors:actor_details', kwargs={'id' :actor.id}))

    else:
        form = ActorForm(instance=actor)  
    
    return render(request, 'actors/actor_edit.html', {'form': form,'actor' :actor})

def delete_actor(request,id):
    actor=Actor.objects.get(id=id)
    actor.delete()
    return redirect(reverse('actors:list-actors'))

"""
api version using rest framework
"""
class ListAndCreateActor(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class=ActorSerializer

class RetrieveUpdateDestroyActor(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class=ActorSerializer
