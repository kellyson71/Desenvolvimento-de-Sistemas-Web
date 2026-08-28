// 17. Reescrevendo a Agenda de Contatos (do exercício 13) usando Classe

class Agenda {
  constructor() {
    this.contatos = [];
  }

  adicionarContato(nome, telefone, categoria) {
    this.contatos.push({ nome, telefone, categoria });
  }

  removerContato(nome) {
    this.contatos = this.contatos.filter(c => c.nome.toLowerCase() !== nome.toLowerCase());
  }

  listarPorCategoria(categoria) {
    return this.contatos.filter(c => c.categoria.toLowerCase() === categoria.toLowerCase());
  }
}

// Demonstração da classe Agenda
let minhaAgenda = new Agenda();
minhaAgenda.adicionarContato("Kellyson", "9999-1111", "pessoal");
minhaAgenda.adicionarContato("Professor", "9999-2222", "faculdade");
minhaAgenda.adicionarContato("Chefe", "9999-3333", "trabalho");

console.log("Contatos de faculdade:", minhaAgenda.listarPorCategoria("faculdade"));

minhaAgenda.removerContato("Chefe");
console.log("Agenda após remover Chefe:", minhaAgenda.contatos);

/*
================================================================================
COMPARAÇÃO ENTRE AS DUAS VERSÕES:
--------------------------------------------------------------------------------
1. Versão procedural (exercício 13):
   - O array 'agenda' fica solto no escopo global (gambiarra). Qualquer função ou
     código pode alterá-lo diretamente e quebrar tudo sem querer.
   - Não dá para ter facilmente mais de uma agenda no mesmo sistema.

2. Versão com Classe (exercício 17):
   - Ficou muito mais organizada porque encapsula os dados dentro da instância
     (this.contatos) e expõe apenas métodos para interagir com eles.
   - Permite instanciar várias agendas independentes (ex: agendaPessoal, agendaTrabalho).
   - O código fica modular, reutilizável e com responsabilidades bem definidas.
================================================================================
*/
