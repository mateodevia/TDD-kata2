from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .models import Portafolio
import json

# Create your views here.
@csrf_exempt
def index(request):
    portafolios_list = Portafolio.objects.all()
    return HttpResponse(serializers.serialize("json", portafolios_list))
