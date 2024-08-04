from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from .models import Article
class ArtcleListView(ListView):
    model=Article
    template_name = 'home.html'

