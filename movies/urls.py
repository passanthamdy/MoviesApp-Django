from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='list-movies'),
    path('<int:id>/details',views.movie_details,name='movie_details' ),
    path('<int:id>/update',views.update_movie,name='movie-update' ),
    path('new/', views.create_movie, name='create_movie'),
    path('<int:id>/delete',views.delete_movie,name='movie-delete' ),
    #api version apis
    path('api/', views.ListCreateMovie.as_view()),
    path('api/<int:pk>/', views.RetrieveUpdateestroyMovie.as_view())


]
