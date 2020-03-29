from django.contrib.auth.management import get_default_username
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from rest_framework.decorators import api_view

from .models import Portafolio
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import json

# Create your views here.
@csrf_exempt
def index(request):
    portafolios_list = Portafolio.objects.all()
    return HttpResponse(serializers.serialize("json", portafolios_list))


@csrf_exempt
def add_user_view(request):
    if request.method == 'POST':
        json_user = json.loads(request.body)
        username = json_user['username']
        first_name = json_user['first_name']
        last_name = json_user['last_name']
        password = json_user['password']
        email = json_user['email']

        user_model = User.objects.create_user(
            username=username, password=password)
        user_model.first_name = first_name
        user_model.last_name = last_name
        user_model.email = email
        user_model.save()
    return HttpResponse(serializers.serialize("json", [user_model]))


def get_portafolios_publicos(request, username):
    usuario = User.objects.get(username=username)
    print(usuario)
    portafolios_list = Portafolio.objects.filter(user=usuario, public=True)
    return HttpResponse(serializers.serialize("json", portafolios_list))


@csrf_exempt
def iniciar_sesion(request):
    json_user = json.loads(request.body)
    username = json_user['username']
    password = json_user['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        # Redirect to a success page.
        return HttpResponse(status=200)
    else:
        # Return an 'invalid login' error message.
        return HttpResponse(status=400)




