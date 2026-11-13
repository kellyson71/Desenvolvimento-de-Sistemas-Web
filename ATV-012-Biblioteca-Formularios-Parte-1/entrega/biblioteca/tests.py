from django.test import Client, TestCase
from django.urls import reverse

from .models import Author


class AuthorCreateTests(TestCase):
    url = reverse("biblioteca:author_create")

    def test_get_mostra_formulario(self):
        resposta = self.client.get(self.url)
        self.assertContains(resposta, "Nome")
        self.assertContains(resposta, "Nacionalidade")
        self.assertContains(resposta, "csrfmiddlewaretoken")

    def test_nome_obrigatorio(self):
        resposta = self.client.post(self.url, {"name": "", "nationality": ""})
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, "Este campo é obrigatório.")
        self.assertEqual(Author.objects.count(), 0)

    def test_nacionalidade_em_branco(self):
        resposta = self.client.post(self.url, {"name": "Machado de Assis", "nationality": ""})
        autor = Author.objects.get()
        self.assertRedirects(resposta, reverse("biblioteca:author_detail", args=[autor.pk]))

    def test_redirect_evita_duplicar_ao_atualizar(self):
        resposta = self.client.post(self.url, {"name": "Clarice Lispector", "nationality": "Brasileira"}, follow=True)
        self.assertContains(resposta, "Clarice Lispector")
        self.client.get(resposta.redirect_chain[-1][0])
        self.assertEqual(Author.objects.count(), 1)

    def test_sem_token_csrf_e_rejeitado(self):
        cliente = Client(enforce_csrf_checks=True)
        resposta = cliente.post(self.url, {"name": "Fulano", "nationality": ""})
        self.assertEqual(resposta.status_code, 403)
        self.assertEqual(Author.objects.count(), 0)

    def test_link_na_lista(self):
        resposta = self.client.get(reverse("biblioteca:listar_livros"))
        self.assertContains(resposta, f'href="{self.url}"')
