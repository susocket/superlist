from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page

# Create your tests here.

class SmokeTest(TestCase):
    def test_bad_method(self):
        self.assertEqual(1+1, 2)

class HomePageTest(TestCase):
    def test_root_rul_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
