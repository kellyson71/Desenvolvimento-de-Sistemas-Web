Biblioteca em Django, continuando a parte 1 (cadastro de autor). Agora tem cadastro e edição de livro com um ModelForm (`BookForm`). A mesma view `book_form` atende `/livros/novo/` e `/livros/<id>/editar/` e as duas usam o template `book_form.html`; sem id ela cria, com id edita, e id que não existe dá 404. Depois de salvar volta para a página do autor do livro.

Validações no `BookForm`: o título tem os espaços sobrando tirados (começo, fim e repetidos no meio) e precisa ficar com pelo menos 3 caracteres; o ano não pode passar do ano atual, que é pego com `date.today().year` na hora de validar.

Para rodar: `pip install django`, `python manage.py migrate` e `python manage.py runserver`. Testes: `python manage.py test`.
