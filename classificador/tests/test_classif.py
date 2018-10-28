from django.test import TestCase
from classificador.utils.classificadores.regex_classif import classificate

# Create your tests here.

class classificateTestCase(TestCase):

    def test_classificate(self):
        content = None
        with open("classificador/tests/t1.html") as f:
            content = f.read()