from django.urls import path

from . import views

app_name="firstapp"

urlpatterns = [
    path('',views.vista,name='vista'),
    path('dogs',views.dogs,name='dogs'),
    path('dog/add',views.dogsAdd,name='dogsAdd'),
    path('dog/delete',views.dogsDelete,name='dogsdelete'),
    path('dog/get',views.dogsGet,name='dogsGet'),
    path('dog/get/<int:dogid>',views.dogsGetId,name='dogsGetId'),
    path('dog/update/<int:dogid>',views.dogsUpdate,name='dogsUpdate'),
    path('types',views.types,name='types'),
    path('videogames',views.videogames,name='videogames'),
    path('videogame/add',views.videogamesAdd,name='videogamesAdd'),
    path('videogame/delete/<int:videogameid>',views.videogamesDelete,name='videogamesdelete'),
    path('videogame/get',views.videogamesGet,name='videogamesGet'),
    path('videogame/get/<int:videogameid>',views.videogamesGetId,name='videogamesGetId'),
    path('videogame/update/<int:videogameid>',views.videogamesUpdate,name='videogamesUpdate'),
    path('rating',views.rating,name='rating'),
    path('rating/add',views.ratingAdd,name='ratingAdd'),
    path('rating/delete',views.ratingDelete,name='ratingdelete'),
    path('add',views.add,name='add'),
    path('delete/<int:videogameid>/<str:videogame>',views.delete,name='delete'),
    path('update/<int:videogameid>',views.update,name='update'),

]
