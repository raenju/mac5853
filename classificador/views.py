from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import Http404
from . import templates
import requests as rq
from . import utils as utl
from .models import *

# Chamadas de renderização das páginas

def index(request):
	vv = [1,2,3,9,8,7]
	context = {'vec':vv}
	return render(request, 'classificador/index.html', context)

def search(request):
	rlist = None
	try:
		rlist = get_list_or_404(Motivo)
	except Http404:
		rlist = None
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
	site_list = utl.parse_url.parse(query)
	for s in site_list:
		vv.append(s)
	sites = [utl.classif.classificate(utl.html_handler.get_html(site)) for site in site_list]

	for entry in sites:
		for reason in entry["reasons"]:
			try:
				e = get_object_or_404(Motivo, nome=reason)
			except Http404:
				mot = Motivo(nome=reason)
				mot.save()


	#sites = [{"url": "site1", "restrict": True, "reasons":["reason1","reason2"]}]
	context = {'vec':vv, 'sites':sites}

	# sites deve ser da forma "sites": [{"url": "site1", "restrict": True, "reasons":["reason1","reason2"]}, {"url": "site2", "restrict": False, "reasons": []}, ]


	if 'callback' in request.POST:
		callback = request.POST['callback']
		r = rq.post(callback, data=sites)
	else:
		return render(request, 'classificador/resposta.html', context)