Biblioteca em Django (continuação da atividade de relacionamentos), agora com cadastro de autor por formulário. A página fica em `/autores/novo/` e a lista de livros tem o link "Novo autor". Depois de salvar, a view redireciona para a página do autor, então dar F5 nela não cadastra de novo.

Para rodar: `pip install django`, `python manage.py migrate` e `python manage.py runserver`. Testes: `python manage.py test`.

Teste do CSRF: tirei o `{% csrf_token %}` do template e mandei o formulário. O Django recusou com 403 Proibido, "Verificação CSRF falhou. Pedido cancelado.", e o autor não foi salvo. Com o token de volta, salva normal. Sem essa proteção qualquer outro site poderia fazer o navegador de quem está logado enviar esse POST sem a pessoa saber.
