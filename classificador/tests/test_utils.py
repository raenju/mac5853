from django.test import TestCase
from classificador.utils.parse_url import get_domain, parse
from classificador.utils.html_handler import get_html

# Create your tests here.

class getDomainTestCase(TestCase):

    def test_get_domain(self):
        google = "https://www.google.com/"
        google2 = "www.google.com"
        google3 = "www.google.com/otherstuff"
        google4 = "https://www.google.com/otherstuff"
        google5 = "https:////www.google.com/otherstuff//"
        self.assertEqual(get_domain(google), 'google.com')
        self.assertEqual(get_domain(google2), 'google.com')
        self.assertEqual(get_domain(google3), 'google.com')
        self.assertEqual(get_domain(google4), 'google.com')
        self.assertEqual(get_domain(google5), 'google.com')

class parseTestCase(TestCase):

    def test_parse(self):
        str1 = "ab cd ef gh /i -j"
        str2 = "a1         e2             c3"
        self.assertEqual(parse(str1), ["ab","cd","ef","gh","/i","-j"])
        self.assertEqual(parse(str2), ["a1","e2","c3"])

class getHtmlTestCase(TestCase):

    def test_get_html(self):
        str1 = "abc"
        str2 = "https://www.google.com/"
        self.assertEqual(get_html(str1).html, None)
        self.assertEqual(get_html(str2).error, None)