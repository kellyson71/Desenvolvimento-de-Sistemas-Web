from django.test import TestCase
from django.urls import reverse

class PageTests(TestCase):
    def test_home_page_status_and_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'core/home.html')
        self.assertContains(response, 'Estúdio Fluxo')
        self.assertContains(response, 'Criamos marcas que as pessoas')
        self.assertContains(response, '/static/css/style.css')
        self.assertNotContains(response, '.html')

    def test_portfolio_page_status_and_template(self):
        response = self.client.get(reverse('portfolio'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'core/portfolio.html')
        self.assertContains(response, 'Portfólio — Estúdio Fluxo')
        self.assertContains(response, 'Projetos que ajudamos a tirar do papel')
        self.assertContains(response, '/static/css/style.css')
        self.assertNotContains(response, '.html')
