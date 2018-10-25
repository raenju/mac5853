import requests

class html_page:
	def __init__(self, url, html, err=None):
		self.url = url
		self.html = html
		self.error = err

def get_html(url):
	r = None
	try:
		r = requests.get(url)
	except requests.exceptions.RequestException as e:
		return html_page(url, None, e)
	return html_page(url, r.text)