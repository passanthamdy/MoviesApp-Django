from django.urls import path
from . import views

app_name = 'actors'

urlpatterns = [
    path('', views.home, name='list-actors'),
    path('<int:id>/details', views.actor_details, name='actor_details'),
    path('<int:id>/update', views.actor_update, name='actor_update'),
    path('new/', views.actor_create, name='add_actor'),
    path('<int:id>/delete', views.delete_actor, name='actor-delete'),
    #api version urls
    path('api/',views.ListAndCreateActor.as_view()),
    path('api/<int:pk>', views.RetrieveUpdateDestroyActor.as_view())


]
