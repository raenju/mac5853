from django.test import TestCase
from classificador.utils.classificadores.regex_classif import classificate
from classificador.utils.html_handler import html_page

# Create your tests here.

class classificateTestCase(TestCase):

	def check(self,site):
		if "Prostituicao" in classificate(site):
			return True
		return False

	def test_classificate(self):
		content = None
		with open("classificador/tests/pro1.html") as f:
			content = f.read()
			site = html_page("",content)
			self.assertEqual(self.check(site), True)