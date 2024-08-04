
from django.urls import path
from . import views
urlpatterns = [

    path('',views.ArtcleListView.as_view(),name='home'),
]