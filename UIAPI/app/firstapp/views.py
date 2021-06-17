# Create your views here.
#IMPORT models

#IMPORT LIBRARIRES/FUNCTIONS
from django.shortcuts import render , HttpResponse, redirect
from django.http import JsonResponse
import json
import requests
#IMPORT DJANGO PASSWORD HASH GENERATOR AND COMPARE
from django.contrib.auth.hashers import make_password, check_password
from .models import Dogs,Types, Videogames, Rating
from django import forms

#check_password(noHashPassword,HashedPassword) this funcion validate if the password match to the hash

#def vista(request):
#    return render(request,'clase.html')



class VideogameForm(forms.ModelForm):
    class Meta:
        model = Videogames #model es igual al modelo del archivo models.py
        fields = [
            'name',
            'genre',
            'rating_id',
            
        ]
        labels = { 
            'name' : 'Nombre', 
            'genre' : 'Genero',
            'rating_id' : 'Rating id',
            
        }
        widgets = {
            'name' : forms.TextInput(attrs={'required': True, 'class': 'form-control'}), #Para validar los campos del form
            'genre' : forms.TextInput(attrs={'required': True, 'class': 'form-control'}),
            'rating_id' : forms.NumberInput(attrs={'required': True, 'class': 'form-control'})
        }

def vista(request):


    
    if request.method == 'GET':

        responseData = {}
        responseData['success'] = 'true'
        responseData['data'] = list(Videogames.objects.all().values())
      
        cuantos = len(responseData['data']);
        return render(request, 'clase.html', {'cuantos': cuantos , "videogames": responseData })

    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'

        cuantos = len(responseData['data']);
        return render(request, 'clase.html', {'cuantos': cuantos , "videogames": responseData })




def dogs(request):

    if request.method == 'GET':

        apikey = request.headers.get('api_key')
        apikey = "33390d09esdioewu0qe0uqu0"
        if apikey is not None:

            if apikey != "33390d09esdioewu0qe0uqu0":
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'API KEY NOT VALID'
                return JsonResponse(responseData, status=400)

            responseData = {}
            responseData['success'] = 'true'
            responseData['key'] = apikey
            responseData['data'] = list(Dogs.objects.all().values())
            return JsonResponse(responseData, status=200)

        responseData = {}
        responseData['success'] = 'false'
        responseData['message'] = 'No api Key'
        return JsonResponse(responseData, status=400)

    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)


def dogsAdd(request):

    if request.method == 'POST':

        try:
            json_object = json.loads(request.body)
            newDog = Dogs(name=json_object['dog_name'], type_id=json_object['dog_type_id'], color=json_object['dog_color'], size= json_object['dog_size'])
            #INSERT INTO dogs (name, type_id,color,size) values ('Solovino',4,'black','big')
            newDog.save()
            responseData = {}
            responseData['success'] = 'true'
            responseData['message'] = 'Dog inserted'
            return JsonResponse(responseData, status=200)
        except ValueError as e:
            responseData = {}
            responseData['success'] = 'false'
            responseData['message'] = 'Invalid Json'
            return JsonResponse(responseData, status=400)

    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

def dogsDelete(request):

    if request.method == 'DELETE':

        try:
            json_object = json.loads(request.body)
            try:
                one_entry = Dogs.objects.get(id=json_object["dog_id"])
            except:
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'The dog_id its not valid'
                return JsonResponse(responseData, status=400)
            Dogs.objects.filter(id=json_object["dog_id"]).delete()
            responseData = {}
            responseData['success'] = 'true'
            responseData['message'] = 'The dog has been deleted'
            return JsonResponse(responseData, status=200)
        except ValueError as e:
            responseData = {}
            responseData['success'] = 'false'
            responseData['data'] = 'Invalid Json'
            return JsonResponse(responseData, status=400)
    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

def dogsGet(request):

    if request.method == 'POST':

        try:
            json_object = json.loads(request.body)
            try:
                one_entry = Dogs.objects.get(id=json_object["dog_id"])
            except:
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'The dog_id its not valid'
                return JsonResponse(responseData, status=400)
            responseData = {}
            responseData['success'] = 'true'
            responseData['data'] = {}
            responseData['data']['name'] = one_entry.name
            responseData['data']['size'] = one_entry.size
            responseData['data']['color'] = one_entry.color
            responseData['data']['type_id'] = one_entry.type_id

            return JsonResponse(responseData, status=200)
        except ValueError as e:
            responseData = {}
            responseData['success'] = 'false'
            responseData['data'] = 'Invalid Json'
            return JsonResponse(responseData, status=400)
    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

def dogsGetId(request, dogid):

    if request.method == 'GET':

        try:
            one_entry = Dogs.objects.get(id=dogid)
        except:
            responseData = {}
            responseData['success'] = 'false'
            responseData['message'] = 'The dog_id its not valid'
            return JsonResponse(responseData, status=400)

        responseData = {}
        responseData['success'] = 'true'
        responseData['data'] = {}
        responseData['data']['name'] = one_entry.name
        responseData['data']['size'] = one_entry.size
        responseData['data']['color'] = one_entry.color
        responseData['data']['type_id'] = one_entry.type_id

        return JsonResponse(responseData, status=200)

    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

def dogsUpdate(request,dogid):

    if request.method == 'POST':
        try:
            one_entry = Dogs.objects.get(id=dogid)
        except:
            responseData = {}
            responseData['success'] = 'false'
            responseData['message'] = 'The dog_id its not valid'
            return JsonResponse(responseData, status=400)
        try:
            json_object = json.loads(request.body)
            contador = 0
            #AQUI VA EL CODIGO DEL UPDATE
            try:
                value = json_object["dog_name"]
                Dogs.objects.filter(id=dogid).update(name=json_object["dog_name"])
                contador = contador + 1
            except KeyError:
                responseData = {}

            try:
                value = json_object["dog_size"]
                Dogs.objects.filter(id=dogid).update(size=json_object["dog_size"])
                contador = contador + 1
            except KeyError:
                responseData = {}

            try:
                value = json_object["dog_color"]
                Dogs.objects.filter(id=dogid).update(color=json_object["dog_color"])
                contador = contador + 1
            except KeyError:
                responseData = {}

            try:
                value = json_object["dog_type"]
                Dogs.objects.filter(id=dogid).update(type_id=json_object["dog_type"])
                contador = contador + 1
            except KeyError:
                responseData = {}

            if contador == 0:
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'Nada por actualizar'
                return JsonResponse(responseData, status=400)
            else:
                responseData = {}
                responseData['success'] = 'true'
                responseData['message'] = 'Datos actualizados'
                return JsonResponse(responseData, status=200)

        except ValueError as e:
            responseData = {}
            responseData['success'] = 'false'
            responseData['data'] = 'Invalid Json'
            return JsonResponse(responseData, status=400)

    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

def types(request):

    if request.method == 'GET':

        responseData = {}
        responseData['success'] = 'true'
        responseData['data'] = list(Types.objects.all().values())
        return JsonResponse(responseData, status=200)

    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

# videogames





def videogames(request):
    
    if request.method == 'GET':

        responseData = {}
        responseData['success'] = 'true'
        responseData['data'] = list(Videogames.objects.all().values())
        return JsonResponse(responseData, status=200)

    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)


def videogamesAdd(request):

    if request.method == 'POST':

      newVideogame = Videogames(name=request.POST.get("name"), genre=request.POST.get("genre"), rating_id=request.POST.get("rating_id"))
      newVideogame.save()
    return redirect('/')

def videogamesDelete(request,videogameid):

    if request.method == 'POST':
        
        Videogames.objects.filter(id=videogameid).delete() #lo que está dentro del filter(id=), ese "id" debe ser escrito igual a como está declarado en mi modelo o bd
        
    return redirect('/')

def videogamesGet(request):

    if request.method == 'POST':

        try:
            json_object = json.loads(request.body)
            try:
                one_entry = Videogames.objects.get(id=json_object["videogame_id"])
            except:
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'The videogame_id its not valid'
                return JsonResponse(responseData, status=400)
            responseData = {}
            responseData['success'] = 'true'
            responseData['data'] = {}
            responseData['data']['name'] = one_entry.name
            responseData['data']['genre'] = one_entry.genre
            responseData['data']['rating_id'] = one_entry.rating_id
           

            return JsonResponse(responseData, status=200)
        except ValueError as e:
            responseData = {}
            responseData['success'] = 'false'
            responseData['data'] = 'Invalid Json'
            return JsonResponse(responseData, status=400)
    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

def videogamesGetId(request, videogameid):

    if request.method == 'GET':
       
        try:
            one_entry = Videogames.objects.get(id=videogameid)
        except:
            responseData = {}
            responseData['success'] = 'false'
            responseData['message'] = 'The videogame_id its not valid'
            return JsonResponse(responseData, status=400)
        
        responseData = {}
        responseData['success'] = 'true'
        responseData['data'] = {}
        responseData['data']['name'] = one_entry.name
        responseData['data']['genre'] = one_entry.genre
        responseData['data']['rating_id'] = one_entry.rating_id

        return JsonResponse(responseData, status=200)
      
    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)




def videogamesUpdate(request, videogameid):
    if request.method == 'POST':
       
        try:
            one_entry = Videogames.objects.get(id=videogameid)
           
        except:
            responseData = {}
            responseData['success'] = 'false'
            responseData['message'] = 'The videogame_id its not valid'
            return JsonResponse(responseData, status=400)
        try:
            json_object = json.loads(request.body)
            contador = 0
            try:
                value = json_object["videogame_name"]
                Videogames.objects.filter(id=videogameid).update(name=json_object["videogame_name"])
                contador = contador + 1
            except KeyError:
                responseData = {}
            try:
                value = json_object["videogame_genre"]
                Videogames.objects.filter(id=videogameid).update(size=json_object["videogame_genre"])
                contador = contador + 1
            except KeyError:
                responseData = {}
            try:
                value = json_object["videogame_rating"]
                Videogames.objects.filter(id=videogameid).update(type_id=json_object["videogame_rating"])
                contador = contador + 1
            except KeyError:
                responseData = {}


            if contador == 0:
                responseData = {}
                responseData['success'] = 'false'
                responseData['mesage'] = 'nada por actuailzar'
                return JsonResponse(responseData, status=200)
            else:
                responseData = {}
                responseData['success'] = 'true'
                responseData['mesage'] = 'datos actualizados'
                return JsonResponse(responseData, status=200)



        except ValueError:
            responseData = {}
            responseData['success'] = 'false'
            responseData['mesage'] = 'invalid json'
            return JsonResponse(responseData, status=400)
        
      
    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

def rating(request):

    if request.method == 'GET':

        responseData = {}
        responseData['success'] = 'true'
        responseData['data'] = list(Rating.objects.all().values())
        return JsonResponse(responseData, status=200)

    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)


def ratingAdd(request):

    if request.method == 'POST':

        try:
            json_object = json.loads(request.body)
            newRating = Rating(esrb=json_object['rating_esrb'], pegi=json_object['rating_pegi'],cero=json_object['rating_cero'])
            newRating.save()
            responseData = {}
            responseData['success'] = 'true'
            responseData['message'] = 'rating inserted'
            return JsonResponse(responseData, status=200)
        except ValueError as e:
            responseData = {}
            responseData['success'] = 'false'
            responseData['message'] = 'Invalid Json'
            return JsonResponse(responseData, status=400)

    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

def ratingDelete(request):

    if request.method == 'DELETE':

        try:
            json_object = json.loads(request.body)
            try:
                one_entry = Rating.objects.get(id=json_object["rating_id"])
            except:
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'The rating_id its not valid'
                return JsonResponse(responseData, status=400)
            Rating.objects.filter(id=json_object["rating_id"]).delete()
            responseData = {}
            responseData['success'] = 'true'
            responseData['message'] = 'The rating has been deleted'
            return JsonResponse(responseData, status=200)
        except ValueError as e:
            responseData = {}
            responseData['success'] = 'false'
            responseData['data'] = 'Invalid Json'
            return JsonResponse(responseData, status=400)
    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)


def add(request):
    form = VideogameForm()
    return render(request, "add.html", {'form' : form} )


def delete(request, videogameid, videogame):
    
    return render(request, "delete.html", {'videogameid': videogameid, 'videogame':videogame} )

def update(request, videogameid):
    
    videogameedit = Videogames.objects.get(id = videogameid)

    if request.method == 'GET':
        form = VideogameForm(instance = videogameedit)
    else:
        form = VideogameForm(request.POST, instance = videogameedit)
        if form.is_valid():
            form.save()
        return redirect('/')




    return render(request, "editar.html", {'videogameid': videogameid, 'form' : form} )