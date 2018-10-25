from django.shortcuts import render
from . import templates
import requests as rq
from . import utils as utl

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
	query = request.POST['sites']
	vv = [1,2,3,9,8,7, query]
	sites = utl.parse_url.parse(query)
	for s in sites:
		vv.append(s)
	#site_list = utl.parse_url.parse(sites)
	context = {'vec':vv, 'sites':sites}

	# sites deve ser da forma "sites": [{"url": "site1", "restrict": True, "reasons":["reason1","reason2"]}, {"url": "site2", "restrict": False, "reasons": []}, ]


	if 'callback' in request.POST:
		callback = request.POST['callback']
		r = rq.post(callback, data=sites)
	else:
		return render(request, 'classificador/index.html', context)