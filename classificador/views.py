from django.shortcuts import render

from . import templates

def index(request):
    context = {}
    return render(request, 'classificador/index.html', context)

def search(request):
	context = {}
	return render(request, 'classificador/busca.html', context)

def answer(request):
	context = {}
	return render(request, 'classificador/resposta.html', context)

def querylist(request):
	context = {}
	return render(request, 'classificador/lista.html', context)