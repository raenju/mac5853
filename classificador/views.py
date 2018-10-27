from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import Http404
from . import templates
import requests as rq
from . import utils as utl
from .models import *

# Chamadas de renderização das páginas

def index(request):
	context = {}
	return render(request, 'classificador/index.html', context)

def search(request):
	rlist = None
	reasons = []
	try:
		rlist = get_list_or_404(Motivo)
	except Http404:
		rlist = None
	if rlist is None:
		reasons = []
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
	sites = []
	for site in site_list:
		req = Requisicao(url=site, status="Na fila de processamento")
		req.save()
		sites.append([site, req])

	for pair in sites:
		req = pair[1]
		req.status = "Em processamento"
		req.save()
		entry = utl.classif.classificate(utl.html_handler.get_html(pair[0]))
		req.status = "Processamento finalizado"
		req.save()
		if "Erro_ao_buscar_o_site" in entry["reasons"]:
			continue
		else:
			domain_url = utl.parse_url.get_domain(entry["url"])
			try:
				dom = get_object_or_404(Dominio, url=domain_url)
				if entry["restrict"] is True and dom.restrict is False:
					dom.restrict = True
					dom.save()
			except Http404:
				dom = Dominio(url=domain_url, restrict=entry["restrict"])
				dom.save()
			try:
				pag = get_object_or_404(Pagina, url=entry["url"])
				if entry["restrict"] is True and pag.restrict is False:
					pag.restrict = True
					pag.save()
			except Http404:
				pag = Pagina(url=entry["url"], domain=dom, restrict=entry["restrict"])
				pag.save()
			for reason in entry["reasons"]:
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
				try:
					e = get_object_or_404(PaginaRestritoPor, id_p=pag, nome_m=mot)
				except Http404:
					prp = PaginaRestritoPor(id_p=pag, nome_m=mot)
					prp.save()


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
	stype = request.POST['searchType']
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
	return render(request, 'classificador/resposta.html', context)

def list_req(request):
	context = {}
	sites = []
	status = request.POST.get("req_status", "Todos")
	if status == "Todos":
		print(1)
	if status == "Na fila":
		print(2)
	if status == "Processando":
		print(3)
	if status == "Processado":
		print(4)
	context = {"sites":sites}
	return render(request, 'classificador/lista.html', context)