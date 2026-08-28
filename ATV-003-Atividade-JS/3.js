// 3. Preço, quantidade, desconto progressivo e resumo
let preco = 50;
let qtd = 7;
let subtotal = preco * qtd;

let desc = 0;
if (subtotal > 300) {
  desc = 0.10;
} else if (subtotal > 100) {
  desc = 0.05;
}

let total = subtotal - (subtotal * desc);

console.log(`
========== RESUMO DO PEDIDO ==========
Preço unitário : R$ ${preco.toFixed(2)}
Quantidade     : ${qtd}
Subtotal       : R$ ${subtotal.toFixed(2)}
Desconto       : ${desc * 100}%
Total a pagar  : R$ ${total.toFixed(2)}
======================================
`);
