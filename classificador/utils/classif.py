def classificate(site):
	if site.error is not None:
		return {"url": site.url, "restrict": False, "reasons":["Erro_ao_buscar_o_site"]}
	else:
		return {"url": site.url, "restrict": True, "reasons":["reason1","reason2"]}