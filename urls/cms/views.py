from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from models import Url
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def acortador(request, fila):
    try:
        urls = Url.objects.get(id=fila)
        return HttpResponseRedirect(urls.original)
    except Url.DoesNotExist:
        return HttpResponseNotFound('Esa url acortada no existe')
    
@csrf_exempt 
def general(request):

    formulario= "Introduce tu url a acortar: <br><form action='' method='POST'><input type='text' name='nombre' value='' /><br/><input type='submit'   value='Enviar' /></form>"

    if request.method == "POST":
        url = request.POST["nombre"]
        if not(url.startswith('http')):
            url= 'http://' + url
        try:
            fila = Url.objects.get(original=url)
            formulario += "<p>La url que esta intentando acortar ya esta acortada</p>"
        except Url.DoesNotExist:
            fila = Url(original=url)
            fila.save()

    lista = Url.objects.all()
    for fila in lista:
        formulario += "<p>127.0.0.1:8000/" + str(fila.id) + " corresponde a " + fila.original + " "
        formulario += "</p>"

    return HttpResponse(formulario)
