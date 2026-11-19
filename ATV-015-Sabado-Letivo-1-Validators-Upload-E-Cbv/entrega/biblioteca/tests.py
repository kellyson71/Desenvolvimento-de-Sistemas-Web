import shutil
import tempfile
from datetime import date
from unittest import mock

from django.db import IntegrityError
from django.db.models import ProtectedError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase, override_settings
from django.urls import reverse

from .models import Author, Book, Category


class AuthorTests(TestCase):
    def test_nacionalidade_e_opcional(self):
        autor = Author.objects.create(name="Machado de Assis")
        self.assertEqual(autor.nationality, "")

    def test_autor_com_livros_nao_pode_ser_apagado(self):
        autor = Author.objects.create(name="Machado de Assis")
        Book.objects.create(title="Dom Casmurro", author=autor, year=1899)
        with self.assertRaises(ProtectedError):
            autor.delete()

    def test_autor_sem_livros_pode_ser_apagado(self):
        autor = Author.objects.create(name="Jorge Amado")
        autor.delete()
        self.assertEqual(Author.objects.count(), 0)

    def test_related_name_books(self):
        autor = Author.objects.create(name="Machado de Assis")
        Book.objects.create(title="Dom Casmurro", author=autor, year=1899)
        Book.objects.create(title="Quincas Borba", author=autor, year=1891)
        self.assertEqual(autor.books.count(), 2)

    def test_autores_ordenados_por_nome(self):
        Author.objects.create(name="Jorge Amado")
        Author.objects.create(name="Clarice Lispector")
        nomes = [a.name for a in Author.objects.all()]
        self.assertEqual(nomes, ["Clarice Lispector", "Jorge Amado"])


class CategoryTests(TestCase):
    def test_nome_unico(self):
        Category.objects.create(name="Romance")
        with self.assertRaises(IntegrityError):
            Category.objects.create(name="Romance")


class BookTests(TestCase):
    def test_livro_pode_ficar_sem_categoria(self):
        autor = Author.objects.create(name="Machado de Assis")
        livro = Book.objects.create(title="Dom Casmurro", author=autor, year=1899)
        self.assertEqual(livro.categories.count(), 0)

    def test_livro_com_varias_categorias(self):
        autor = Author.objects.create(name="Machado de Assis")
        livro = Book.objects.create(title="Dom Casmurro", author=autor, year=1899)
        livro.categories.set([Category.objects.create(name="Romance"), Category.objects.create(name="Clássico")])
        self.assertEqual(livro.categories.count(), 2)


class AuthorCreateTests(TestCase):
    url = reverse("biblioteca:author_create")

    def test_formulario_com_rotulos_em_portugues(self):
        resposta = self.client.get(self.url)
        self.assertContains(resposta, "Nome")
        self.assertContains(resposta, "Nacionalidade")
        self.assertContains(resposta, "csrfmiddlewaretoken")

    def test_nome_obrigatorio(self):
        resposta = self.client.post(self.url, {"name": "", "nationality": "Brasileira"})
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, "Este campo é obrigatório.")
        self.assertEqual(Author.objects.count(), 0)

    def test_nacionalidade_pode_ficar_em_branco(self):
        resposta = self.client.post(self.url, {"name": "Machado de Assis", "nationality": ""})
        autor = Author.objects.get()
        self.assertRedirects(resposta, reverse("biblioteca:author_detail", args=[autor.pk]))

    def test_atualizar_a_pagina_do_autor_nao_cria_de_novo(self):
        resposta = self.client.post(self.url, {"name": "Clarice Lispector", "nationality": "Brasileira"}, follow=True)
        self.assertContains(resposta, "Clarice Lispector")
        self.client.get(resposta.redirect_chain[-1][0])
        self.assertEqual(Author.objects.count(), 1)

    def test_sem_token_csrf_o_post_e_recusado(self):
        cliente = Client(enforce_csrf_checks=True)
        resposta = cliente.post(self.url, {"name": "Fulano", "nationality": ""})
        self.assertEqual(resposta.status_code, 403)
        self.assertEqual(Author.objects.count(), 0)

    def test_link_novo_autor_na_lista(self):
        resposta = self.client.get(reverse("biblioteca:listar_livros"))
        self.assertContains(resposta, f'href="{self.url}"')


class BookFormTests(TestCase):
    url_novo = reverse("biblioteca:book_create")

    def setUp(self):
        self.machado = Author.objects.create(name="Machado de Assis")
        self.clarice = Author.objects.create(name="Clarice Lispector")
        self.romance = Category.objects.create(name="Romance")
        self.classico = Category.objects.create(name="Clássico")

    def dados(self, **extra):
        dados = {"title": "Dom Casmurro", "author": self.machado.pk, "year": 1899, "available": "on"}
        dados.update(extra)
        return dados

    def test_novo_livro_mostra_formulario_vazio(self):
        resposta = self.client.get(self.url_novo)
        self.assertContains(resposta, "<title>Novo livro</title>", html=True)
        self.assertContains(resposta, "Cadastrar livro")
        self.assertContains(resposta, 'type="checkbox" name="categories"', count=2)

    def test_cria_livro_e_volta_para_o_autor(self):
        resposta = self.client.post(self.url_novo, self.dados(categories=[self.romance.pk, self.classico.pk]))
        livro = Book.objects.get()
        self.assertRedirects(resposta, reverse("biblioteca:author_detail", args=[self.machado.pk]))
        self.assertEqual(livro.categories.count(), 2)

    def test_livro_sem_categoria_e_aceito(self):
        self.client.post(self.url_novo, self.dados())
        self.assertEqual(Book.objects.get().categories.count(), 0)

    def test_editar_abre_preenchido(self):
        livro = Book.objects.create(title="Quincas Borba", author=self.machado, year=1891)
        livro.categories.add(self.romance)
        resposta = self.client.get(reverse("biblioteca:book_edit", args=[livro.pk]))
        self.assertContains(resposta, "<title>Editar livro</title>", html=True)
        self.assertContains(resposta, "Salvar alterações")
        self.assertContains(resposta, 'value="Quincas Borba"')
        self.assertContains(resposta, 'value="1891"')
        self.assertEqual(resposta.context["form"].instance, livro)

    def test_editar_salva_no_mesmo_livro(self):
        livro = Book.objects.create(title="A hora da estrela", author=self.machado, year=1977)
        resposta = self.client.post(
            reverse("biblioteca:book_edit", args=[livro.pk]),
            self.dados(title="A hora da estrela", author=self.clarice.pk, year=1977, categories=[self.romance.pk]),
        )
        self.assertRedirects(resposta, reverse("biblioteca:author_detail", args=[self.clarice.pk]))
        livro.refresh_from_db()
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(livro.author, self.clarice)
        self.assertEqual(list(livro.categories.all()), [self.romance])

    def test_editar_livro_inexistente_da_404(self):
        resposta = self.client.get(reverse("biblioteca:book_edit", args=[999]))
        self.assertEqual(resposta.status_code, 404)
        resposta = self.client.post(reverse("biblioteca:book_edit", args=[999]), self.dados())
        self.assertEqual(resposta.status_code, 404)

    def test_titulo_tem_espacos_limpos(self):
        self.client.post(self.url_novo, self.dados(title="   Memórias   póstumas  de   Brás Cubas  "))
        self.assertEqual(Book.objects.get().title, "Memórias póstumas de Brás Cubas")

    def test_titulo_curto_depois_da_limpeza(self):
        resposta = self.client.post(self.url_novo, self.dados(title="   O    "))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, "pelo menos 3 caracteres")
        self.assertFalse(Book.objects.exists())

    def test_titulo_com_3_caracteres_passa(self):
        self.client.post(self.url_novo, self.dados(title=" a  b "))
        self.assertEqual(Book.objects.get().title, "a b")

    def test_ano_no_futuro_e_recusado(self):
        ano_que_vem = date.today().year + 1
        resposta = self.client.post(self.url_novo, self.dados(year=ano_que_vem))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, f"O ano precisa estar entre 1450 e {date.today().year}")
        self.assertFalse(Book.objects.exists())

    def test_ano_atual_passa(self):
        self.client.post(self.url_novo, self.dados(year=date.today().year))
        self.assertTrue(Book.objects.exists())

    def test_ano_atual_e_calculado_na_hora(self):
        with mock.patch("biblioteca.validators.date") as falso:
            falso.today.return_value = date(2040, 1, 1)
            resposta = self.client.post(self.url_novo, self.dados(year=2035))
        self.assertEqual(resposta.status_code, 302)

    def test_sem_autor_mostra_erro_no_formulario(self):
        resposta = self.client.post(self.url_novo, self.dados(author=""))
        self.assertContains(resposta, "Escolha o autor do livro")
        self.assertFalse(Book.objects.exists())

    def test_links_editar_e_novo_livro(self):
        livro = Book.objects.create(title="Dom Casmurro", author=self.machado, year=1899)
        url_editar = reverse("biblioteca:book_edit", args=[livro.pk])
        lista = self.client.get(reverse("biblioteca:listar_livros"))
        self.assertContains(lista, f'href="{self.url_novo}"')
        self.assertContains(lista, f'href="{url_editar}"')
        autor = self.client.get(reverse("biblioteca:author_detail", args=[self.machado.pk]))
        self.assertContains(autor, f'href="{url_editar}"')


class ValidadoresTests(BookFormTests):
    def test_ano_antes_de_1450_e_recusado(self):
        resposta = self.client.post(self.url_novo, self.dados(year=1449))
        self.assertContains(resposta, "entre 1450")
        self.assertFalse(Book.objects.exists())

    def test_ano_1450_passa(self):
        self.client.post(self.url_novo, self.dados(year=1450))
        self.assertTrue(Book.objects.exists())

    def test_paginas_de_1_a_5000(self):
        for paginas, ok in [(0, False), (1, True), (5000, True), (5001, False)]:
            with self.subTest(paginas=paginas):
                Book.objects.all().delete()
                self.client.post(self.url_novo, self.dados(pages=paginas))
                self.assertEqual(Book.objects.exists(), ok)

    def test_paginas_e_isbn_sao_opcionais(self):
        self.client.post(self.url_novo, self.dados(pages="", isbn=""))
        livro = Book.objects.get()
        self.assertIsNone(livro.pages)
        self.assertEqual(livro.isbn, "")

    def test_isbn_com_13_digitos(self):
        for isbn, ok in [("9788535902778", True), ("978853590277", False), ("97885359027789", False), ("97885359027ab", False)]:
            with self.subTest(isbn=isbn):
                Book.objects.all().delete()
                self.client.post(self.url_novo, self.dados(isbn=isbn))
                self.assertEqual(Book.objects.exists(), ok)

    def test_titulo_igual_ao_autor(self):
        resposta = self.client.post(self.url_novo, self.dados(title="  machado de assis "))
        self.assertContains(resposta, "não pode ser igual ao nome do autor")
        self.assertFalse(Book.objects.exists())

    def test_indisponivel_exige_isbn(self):
        dados = self.dados(isbn="")
        del dados["available"]
        resposta = self.client.post(self.url_novo, dados)
        self.assertContains(resposta, "indisponível precisa ter o ISBN")
        dados["isbn"] = "9788535902778"
        self.client.post(self.url_novo, dados)
        self.assertFalse(Book.objects.get().available)


class CapaTests(BookFormTests):
    def setUp(self):
        super().setUp()
        self.pasta = tempfile.mkdtemp()
        self.override = override_settings(MEDIA_ROOT=self.pasta)
        self.override.enable()
        self.addCleanup(shutil.rmtree, self.pasta, True)
        self.addCleanup(self.override.disable)

    def imagem(self, nome="capa.png", tamanho_extra=0):
        import io

        from PIL import Image

        buffer = io.BytesIO()
        Image.new("RGB", (10, 10), "red").save(buffer, format="PNG")
        return SimpleUploadedFile(nome, buffer.getvalue() + b"\0" * tamanho_extra, content_type="image/png")

    def test_envia_capa_e_mostra_na_lista_e_no_detalhe(self):
        self.client.post(self.url_novo, self.dados(capa=self.imagem()))
        livro = Book.objects.get()
        self.assertTrue(livro.capa.name.startswith("capas/"))
        self.assertContains(self.client.get(reverse("biblioteca:listar_livros")), livro.capa.url)
        self.assertContains(self.client.get(reverse("biblioteca:book_detail", args=[livro.pk])), livro.capa.url)

    def test_capa_maior_que_1mb(self):
        resposta = self.client.post(self.url_novo, self.dados(capa=self.imagem(tamanho_extra=1024 * 1024)))
        self.assertContains(resposta, "o limite é 1 MB")
        self.assertFalse(Book.objects.exists())

    def test_arquivo_que_nao_e_imagem(self):
        txt = SimpleUploadedFile("capa.txt", b"oi", content_type="text/plain")
        resposta = self.client.post(self.url_novo, self.dados(capa=txt))
        self.assertEqual(resposta.status_code, 200)
        self.assertFalse(Book.objects.exists())

    def test_extensao_nao_permitida(self):
        resposta = self.client.post(self.url_novo, self.dados(capa=self.imagem("capa.gif")))
        self.assertContains(resposta, "jpg, jpeg ou png")
        self.assertFalse(Book.objects.exists())

    def test_formulario_tem_enctype_multipart(self):
        self.assertContains(self.client.get(self.url_novo), 'enctype="multipart/form-data"')


class CbvTests(TestCase):
    def setUp(self):
        self.autor = Author.objects.create(name="Machado de Assis")
        self.livro = Book.objects.create(title="Dom Casmurro", author=self.autor, year=1899)

    def test_lista_ordenada_por_titulo(self):
        Book.objects.create(title="Auto da Compadecida", author=self.autor, year=1955)
        resposta = self.client.get(reverse("biblioteca:listar_livros"))
        self.assertEqual([l.title for l in resposta.context["livros"]], ["Auto da Compadecida", "Dom Casmurro"])

    def test_detalhe_e_404(self):
        self.assertContains(self.client.get(reverse("biblioteca:book_detail", args=[self.livro.pk])), "Dom Casmurro")
        self.assertEqual(self.client.get(reverse("biblioteca:book_detail", args=[999])).status_code, 404)

    def test_exclusao_pede_confirmacao_e_so_apaga_no_post(self):
        url = reverse("biblioteca:book_delete", args=[self.livro.pk])
        resposta = self.client.get(url)
        self.assertTemplateUsed(resposta, "biblioteca/livro_confirm_delete.html")
        self.assertTrue(Book.objects.exists())
        resposta = self.client.post(url)
        self.assertRedirects(resposta, reverse("biblioteca:listar_livros"))
        self.assertFalse(Book.objects.exists())

    def test_excluir_inexistente_da_404(self):
        self.assertEqual(self.client.post(reverse("biblioteca:book_delete", args=[999])).status_code, 404)

    def test_sobre_mostra_totais(self):
        Book.objects.create(title="Quincas Borba", author=self.autor, year=1891, available=False, isbn="9788535902778")
        resposta = self.client.get(reverse("biblioteca:sobre"))
        self.assertEqual(resposta.context["total"], 2)
        self.assertEqual(resposta.context["disponiveis"], 1)
