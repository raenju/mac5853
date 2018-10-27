import importlib
import threading
from . import configs

class ThreadExec(threading.Thread):
	def __init__(self, tid, site, mod, res, lock):
		threading.Thread.__init__(self)
		self.tid = tid
		self.data = site
		self.module = mod
		self.result = res
		self.lock = lock
	def run(self):
		ans = self.module.classificate(self.data)
		self.lock.acquire()
		self.result[self.tid] = ans
		self.lock.release()

def classificate(site):
	if site.error is not None:
		return {"url": site.url, "restrict": False, "reasons":["Erro_ao_buscar_o_site"]}
	else:
		index = 0
		result = [None for i in range(len(configs.filenames))]
		threadLock = threading.Lock()
		threads = []
		for fn in configs.filenames:
			imp = ".classificadores." + fn
			mod = importlib.import_module(imp, package="classificador.utils")
			thr = ThreadExec(index, site, mod, result, threadLock)
			thr.start()
			threads.append(thr)
			index = index + 1
		for t in threads:
			t.join()
		reasons = []
		for i in range(len(result)):
			if result[i] is not None:
				reasons = list(set(reasons) | set(result[i]))
		return {"url": site.url, "restrict": len(reasons)>0, "reasons":reasons}