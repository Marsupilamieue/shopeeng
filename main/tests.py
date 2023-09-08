from django.test import TestCase, Client
from .urls import show_main

# Create your tests here.

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_main_page_contains_expected_content(self):
        response = Client().get('/main/')
        self.assertContains(response, 'Shopeeng')
    
    def test_main_page_context_data(self):
        response = Client().get('/main/')
        self.assertEqual(response.context['name'], 'Faris Zhafir Faza')
        