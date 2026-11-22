Biblioteca em Django (continuação da ATV-014), agora rodando sobre PostgreSQL. Usuário, senha, host e porta do banco, além de SECRET_KEY e DEBUG, vêm de um arquivo `.env` lido com python-decouple. O `.env` não vai para o repositório.

Para rodar: `pip install -r requirements.txt`, copie `.env.example` para `.env` e preencha com os dados do seu banco, depois `python manage.py migrate` e `python manage.py runserver`.

O banco e o usuário precisam existir antes (`CREATE USER` e `CREATE DATABASE` no psql). Para trazer dados do SQLite: `dumpdata` no projeto antigo e `loaddata` neste. Testes: `python manage.py test` (o usuário do banco precisa de CREATEDB).
