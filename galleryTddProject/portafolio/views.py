from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .models import Portafolio
import json

# Create your views here.
@csrf_exempt
def index(request):
    return HttpResponse(serializers.serialize("json", []))
