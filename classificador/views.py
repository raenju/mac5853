from django.shortcuts import render

from . import templates

def index(request):
    context = {}
    return render(request, 'classificador/index.html', context)