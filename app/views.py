"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .models import Participantes

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def participantes(request):
    """Renders the members page."""
    assert isinstance(request, HttpRequest)
    lista_participantes = {}
    lista_participantes = Participantes.objects.all()
    return render(
        request,
        'app/participantes.html',
        {
            'title':'Galeria dos Participantes',
            'message':'Olá! Esta é a galeria dos participantes da Embaixada MeuSucesso.com de Sorocaba!.',
            'year':datetime.now().year,
            'participantes': lista_participantes,
        }
    )


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

