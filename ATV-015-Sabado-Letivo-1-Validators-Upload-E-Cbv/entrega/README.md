Mini biblioteca em Django, em cima da atividade de formulários. Agora o Book tem validadores (título, ano, páginas, ISBN), upload de capa (jpg/jpeg/png até 1 MB) e as views viraram Class-Based Views, com detalhe, exclusão com confirmação e a página /sobre/.

Para rodar: `pip install django pillow`, `python manage.py migrate` e `python manage.py runserver`. As capas ficam na pasta `media/`. Testes: `python manage.py test`.
