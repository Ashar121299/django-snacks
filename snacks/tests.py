from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class snacksTest(TestCase):
    def test_homePage_status(self):
        url=reverse('home')
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
    def test_homepage_template(self):
        url=reverse('home')
        response=self.client.get(url)
        self.assertTemplateUsed(response,'home.html')
    def test_aboutPage_status(self):
        url=reverse('about')
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
    def test_aboutpage_template(self):
        url=reverse('about')
        response=self.client.get(url)
        self.assertTemplateUsed(response,'about.html')

