from django.urls import path
from . import views

urlpatterns = [
    path("jan" , views.jan , name = "index_page"),
    path("feb" , views.feb , name = "index_page"),
    path("mar" , views.mar , name = "index_page"),
    path("apr" , views.apr , name = "index_page"),
    path("may" , views.may , name = "index_page"),
    path("jun" , views.jun , name = "index_page"),
    path("jul" , views.jul , name = "index_page"),
    path("aug" , views.aug , name = "index_page"),
    path("sep" , views.sep , name = "index_page"),
    path("oct" , views.oct , name = "index_page"),
    path("nov" , views.nov , name = "index_page"),
    path("dec" , views.dec , name = "index_page"),
    
]
