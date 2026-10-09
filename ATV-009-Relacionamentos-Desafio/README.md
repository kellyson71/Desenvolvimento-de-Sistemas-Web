Biblioteca em Django onde um livro pode ter mais de um autor. O campo `author` (ForeignKey) virou `authors` (ManyToMany) sem apagar o banco, em três migrações: a 0003 cria o campo novo, a 0004 copia o autor de cada livro com RunPython e a 0005 remove o campo antigo.

Para rodar: `pip install django`, `python manage.py migrate` e `python manage.py runserver`. A lista fica em `/` e o cadastro em `/admin/`. Os prints do admin antes e depois da migração estão em `prints/`.

Que dados se perdem quando a migração é revertida? Os coautores. O ForeignKey só guarda um autor por livro, então na volta cada livro fica só com o primeiro autor em ordem alfabética e os outros vínculos somem, porque a tabela `biblioteca_book_authors` é apagada. Esse primeiro pode nem ser o autor que o livro tinha antes.

O que acontece com o livro quando o único autor é apagado? Nada impede. O Django apaga só a linha da tabela intermediária e o livro continua existindo, sem autor nenhum. Antes isso não acontecia porque o ForeignKey tinha `on_delete=PROTECT`, e o ManyToMany não tem `on_delete`. Para garantir pelo menos um autor, o campo `authors` fica sem `blank=True`, assim o formulário do admin não deixa salvar livro sem autor. Na hora de apagar um autor é preciso conferir antes se algum livro só tem ele e bloquear a exclusão, por exemplo sobrescrevendo o `delete()` de `Author`.
