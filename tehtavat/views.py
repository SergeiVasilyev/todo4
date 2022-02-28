from django.http import HttpResponse
from django.shortcuts import render

def etusivu(request):
    response = render(request, "etusivu.html")
    return response

def tietoa(request):
    response = render(request, "tietoa.html")
    return response

def yhteystiedot(request):
    return HttpResponse("<html><body>yhteystiedot</body></html>")
