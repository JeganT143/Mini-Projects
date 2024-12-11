from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def jan(request):
    return HttpResponse("<h1>January</h1>")
def feb(request):
    return HttpResponse("<h1>February</h1>")
def mar(request):
    return HttpResponse("<h1>March</h1>")
def apr(request):
    return HttpResponse("<h1>April</h1>")
def may(request):
    return HttpResponse("<h1>May</h1>")
def jun(request):
    return HttpResponse("<h1>June</h1>")
def jul(request):
    return HttpResponse("<h1>July</h1>")
def aug(request):
    return HttpResponse("<h1>August</h1>")
def sep(request):
    return HttpResponse("<h1>September</h1>")
def oct(request):
    return HttpResponse("<h1>October</h1>")
def nov(request):
    return HttpResponse("<h1>November</h1>")
def dec(request):
    return HttpResponse("<h1>December</h1>")

