from django.shortcuts import render
from . import templates


# Chamadas de renderização das páginas

def index(request):
	vv = [1,2,3,9,8,7]
	context = {'vec':vv}
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


# Chamadas de formulários

def urls_submit(request):
	query = request.POST['url_list']
	vv = [1,2,3,9,8,7, query]
	context = {'vec':vv}
	return render(request, 'classificador/index.html', context)