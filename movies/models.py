
from django.db import models
from actors.models import Actor
# Create your models here.

class Director(models.Model):
    name=models.CharField( max_length=50)

    def __str__(self):
        return self.name
    

class Movie(models.Model):
    director=models.ForeignKey("movies.Director", verbose_name="Director", on_delete=models.CASCADE)
    name=models.CharField( max_length=50)
    production_year=models.PositiveSmallIntegerField(blank=True, null=True)
    image= models.ImageField(upload_to='movies/', default='img.png') 
    actors=models.ManyToManyField("actors.Actor",)
    created_at=models.DateField(  auto_now_add=True)
    updated_at=models.DateField( auto_now=True)

    def __str__(self):
        return self.name
    

