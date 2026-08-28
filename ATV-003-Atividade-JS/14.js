// 14. Classe Produto
class Produto {
  constructor(nome, preco, quantidade) {
    this.nome = nome;
    this.preco = preco;
    this.quantidade = quantidade;
  }

  aplicarDesconto(porcentagem) {
    this.preco -= this.preco * (porcentagem / 100);
  }

  estaDisponivel() {
    return this.quantidade > 0;
  }
}

// Três instâncias
let prod1 = new Produto("Teclado Gamer", 150, 10);
let prod2 = new Produto("Mouse sem fio", 80, 0);
let prod3 = new Produto("Monitor", 900, 3);

console.log(`${prod1.nome} disponível?`, prod1.estaDisponivel());
console.log(`${prod2.nome} disponível?`, prod2.estaDisponivel());

console.log(`Preço original do ${prod1.nome}: R$ ${prod1.preco}`);
prod1.aplicarDesconto(10);
console.log(`Preço com 10% de desconto: R$ ${prod1.preco}`);

prod3.aplicarDesconto(20);
console.log(`Preço do ${prod3.nome} com 20% de desconto: R$ ${prod3.preco}`);
