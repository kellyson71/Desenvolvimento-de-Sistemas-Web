// 12. Funções de controle de estoque
let estoque = [
  { nome: "Arroz", preco: 25.5, qtd: 10 },
  { nome: "Feijão", preco: 8.0, qtd: 4 },
  { nome: "Picanha", preco: 79.9, qtd: 2 },
  { nome: "Miojo", preco: 2.5, qtd: 50 },
  { nome: "Óleo", preco: 6.0, qtd: 3 }
];

function totalEstoque(prods) {
  let total = 0;
  for (let p of prods) {
    total += p.preco * p.qtd;
  }
  return total;
}

function maisCaro(prods) {
  let maior = prods[0];
  for (let p of prods) {
    if (p.preco > maior.preco) {
      maior = p;
    }
  }
  return maior;
}

function estoqueAbaixoDe(prods, minimo) {
  return prods.filter(p => p.qtd < minimo);
}

console.log("Valor total do estoque: R$", totalEstoque(estoque));
console.log("Produto mais caro:", maisCaro(estoque));
console.log("Produtos com qtd abaixo de 5:", estoqueAbaixoDe(estoque, 5));
