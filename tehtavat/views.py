from multiprocessing import context
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import Tehtava

def etusivu(request):
    tiedot = {
        "tehtavat": Tehtava.objects.all(),
    }
    response = render(request, "etusivu.html", tiedot)
    return response

def tehatava_sivu(request, id):
    try:
        tehtava = Tehtava.objects.get(id=id)
    except Tehtava.DoesNotExist:
        return HttpResponseNotFound(f"Tehtava {id} ei löydy")
    context = {"tehtava": tehtava}
    return render(request, "tehtava.html", context)
    # return HttpResponse(f"Tehtava {id} on {tehtava}")

def tietoa(request):
    response = render(request, "tietoa.html")
    return response

def yhteystiedot(request):
    return HttpResponse("<html><body>yhteystiedot</body></html>")
