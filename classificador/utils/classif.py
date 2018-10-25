import importlib
from . import configs

def classificate(site):
	if site.error is not None:
		return {"url": site.url, "restrict": False, "reasons":["Erro_ao_buscar_o_site"]}
	else:
		for fn in configs.filenames:
			imp = ".classificadores." + fn
			mod = importlib.import_module(imp, package="classificador.utils")
			mod.classificate(1) # Deveria devolver o resultado
		return {"url": site.url, "restrict": True, "reasons":["reason1","reason2"]}

