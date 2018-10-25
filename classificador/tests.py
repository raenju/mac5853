from django.test import TestCase
from .utils.parse_url import get_domain

# Create your tests here.

class getDomainTestCase(TestCase):

    def test_get_domain(self):
        google = "https://www.google.com/"
        google2 = "www.google.com"
        google3 = "www.google.com/otherstuff"
        google4 = "https://www.google.com/otherstuff"
        self.assertEqual(get_domain(google), 'google.com')
        self.assertEqual(get_domain(google2), 'google.com')
        self.assertEqual(get_domain(google3), 'google.com')
        self.assertEqual(get_domain(google4), 'google.com')