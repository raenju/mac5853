def classificate(site):
	if site.error is not None:
		return {"url": site.url, "restrict": False, "reasons":["Erro ao buscar o site"]}
	else:
		return {"url": site.url, "restrict": True, "reasons":[]}