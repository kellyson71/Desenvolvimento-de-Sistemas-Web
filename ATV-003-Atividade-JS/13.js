// 13. Agenda de contatos e valores únicos

let agenda = [
  { nome: "João", telefone: "9999-1111", categoria: "trabalho" },
  { nome: "Maria", telefone: "9999-2222", categoria: "familia" }
];

function adicionarContato(nome, telefone, categoria) {
  agenda.push({ nome, telefone, categoria });
}

function removerContato(nome) {
  agenda = agenda.filter(c => c.nome.toLowerCase() !== nome.toLowerCase());
}

function listarPorCategoria(categoria) {
  return agenda.filter(c => c.categoria.toLowerCase() === categoria.toLowerCase());
}

// Demonstração da agenda
adicionarContato("Kellyson", "9999-3333", "amigos");
adicionarContato("Pedro", "9999-4444", "trabalho");
console.log("Contatos de trabalho:", listarPorCategoria("trabalho"));

removerContato("Maria");
console.log("Agenda após remover Maria:", agenda);

// Extra da questão 13: Array com valores únicos (gambiarra do Set)
function valoresUnicos(arr) {
  return [...new Set(arr)];
}

let numeros = [1, 2, 2, 3, 4, 4, 5, 1, 6, 7, 7];
console.log("Array original:", numeros);
console.log("Valores únicos:", valoresUnicos(numeros));
