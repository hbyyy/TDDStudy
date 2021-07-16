from django.http import HttpRequest
from django.test import TestCase

# Create your tests here.
from django.urls import resolve
from .views import index


class IndexPageTest(TestCase):

    def test_root_url_resolver_to_index_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_index_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
