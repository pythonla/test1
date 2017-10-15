from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    city = AreaInfo.objects.get(atitle='广州市')
    