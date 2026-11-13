Biblioteca em Django, agora com cadastro de autores por formulário (`AuthorForm`, um ModelForm). A página fica em `/autores/novo/` e o link "Novo autor" está na lista de livros. Depois de salvar, a view faz redirect para a página do autor, então F5 não cria outro.

Para rodar: `pip install django`, `python manage.py migrate` e `python manage.py runserver`. Os testes: `python manage.py test`.

Sem o `{% csrf_token %}` no template, o POST é recusado pelo Django com erro 403 (Forbidden, "CSRF verification failed") e o autor não é salvo. O teste `test_sem_token_csrf_e_rejeitado` confere isso. Sem essa proteção, qualquer outro site poderia enviar um POST para essa URL usando o navegador do usuário e cadastrar autores sem ele perceber.
