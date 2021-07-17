from django.http import HttpRequest
from django.test import TestCase

# Create your tests here.
from django.urls import resolve, reverse
from .views import home_page


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'lists/home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post(reverse('home'), {'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode('utf8'))
        self.assertTemplateUsed(response, 'lists/home.html')
