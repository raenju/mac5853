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
	reasons = []
	try:
		rlist = get_list_or_404(Motivo)
	except Http404:
		rlist = None
	if rlist is None:
		pass ############################
	else:
		reasons = [reason.nome for reason in rlist]
	context = {'reasons':reasons}
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
	site_list = utl.parse_url.parse(query)
	sites = [utl.classif.classificate(utl.html_handler.get_html(site)) for site in site_list]

	for entry in sites:
		try:
			dom = get_object_or_404(Dominio, url=entry["url"])
			if entry["restrict"] is True and dom.restrict is False:
				dom.restrict = True
				dom.save()
		except Http404:
			dom = Dominio(url=entry["url"], restrict=entry["restrict"])
			dom.save()

		for reason in entry["reasons"]:
			if reason == "Erro_ao_buscar_o_site":
				break
			try:
				mot = get_object_or_404(Motivo, nome=reason)
			except Http404:
				mot = Motivo(nome=reason)
				mot.save()
			try:
				e = get_object_or_404(DominioRestritoPor, id_d=dom, nome_m=mot)
			except Http404:
				drp = DominioRestritoPor(id_d=dom, nome_m=mot)
				drp.save()


	#sites = [{"url": "site1", "restrict": True, "reasons":["reason1","reason2"]}]
	context = {'sites':sites}

	# sites deve ser da forma "sites": [{"url": "site1", "restrict": True, "reasons":["reason1","reason2"]}, {"url": "site2", "restrict": False, "reasons": []}, ]


	if 'callback' in request.POST:
		callback = request.POST['callback']
		r = rq.post(callback, data=sites)
	else:
		return render(request, 'classificador/resposta.html', context)

def search_submit(request):
	context = {}
	slist = request.POST.getlist('searchlist')
	print(slist)
	stype = request.POST['searchType'] # "AND" ou "OR"
	if not slist:
		context = {"sites":[]}
	else:
		if stype == "AND":
			result = []
			try:
				sites = get_list_or_404(Dominio)
			except Http404:
				sites = []
			if not sites:
				context = {"sites":[]}
			else:
				for site in sites:
					try:
						motivosDom = get_list_or_404(DominioRestritoPor, id_d=site)
					except Http404:
						motivosDom = []
					if not motivosDom:
						continue
					else:
						motivos = []
						for motivo in motivosDom:
							mot = get_object_or_404(Motivo, nome=motivo.nome_m.nome)
							motivos.append(mot.nome)
						if set(slist)<=set(motivos):
							result.append({"url":site.url, "restrict": True, "reasons":motivos})
			context = {"sites":result}
			return render(request, 'classificador/resposta.html', context)

		else:
			result = []
			try:
				sites = get_list_or_404(Dominio)
			except Http404:
				sites = []
			if not sites:
				context = {"sites":[]}
			else:
				for site in sites:
					try:
						motivosDom = get_list_or_404(DominioRestritoPor, id_d=site)
					except Http404:
						motivosDom = []
					if not motivosDom:
						continue
					else:
						motivos = []
						for motivo in motivosDom:
							mot = get_object_or_404(Motivo, nome=motivo.nome_m.nome)
							motivos.append(mot.nome)
						flag_s = False
						for r in slist:
							if r in motivos:
								flag_s = True
								break
						if flag_s:
							result.append({"url":site.url, "restrict": True, "reasons":motivos})
			context = {"sites":result}
			return render(request, 'classificador/resposta.html', context)
	return render(request, 'classificador/index.html', context)