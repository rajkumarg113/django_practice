from django.shortcuts import render
from django.http import HttpResponse,request
# Create your views here.
def home(request):
    return HttpResponse("hola means hellow in spanish")
def abc(request):
    return HttpResponse("hola means  abc")

