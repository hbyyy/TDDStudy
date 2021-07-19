from django.http import HttpRequest
from django.test import TestCase

# Create your tests here.
from django.urls import resolve, reverse
from .models import Item


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'lists/home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post(reverse('home'), {'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirect_after_POST(self):
        response = self.client.post(reverse('home'), {'item_text': 'test redirect item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/the-only-list/')

    def test_only_saves_item_when_post(self):
        self.client.get(reverse('home'))
        self.assertEqual(Item.objects.count(), 0)


class ItemModelTest(TestCase):
    def test_saving_and_retrieving_item(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')


class ListViewTest(TestCase):

    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list/')
        self.assertTemplateUsed(response, 'lists/list.html')

    def test_displays_all_item(self):
        Item.objects.create(text='item 1')
        Item.objects.create(text='item 2')

        response = self.client.get('/lists/the-only-list/')

        self.assertContains(response, 'item 1')
        self.assertContains(response, 'item 2')
