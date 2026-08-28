// 5. Calculadora com switch/case
function calc(a, b, op) {
  switch (op) {
    case '+':
      return a + b;
    case '-':
      return a - b;
    case '*':
      return a * b;
    case '/':
      if (b === 0) return "Erro: divisão por zero não rola!";
      return a / b;
    default:
      return "Operador inválido!";
  }
}

console.log("10 + 5 =", calc(10, 5, '+'));
console.log("10 - 5 =", calc(10, 5, '-'));
console.log("10 * 5 =", calc(10, 5, '*'));
console.log("10 / 2 =", calc(10, 2, '/'));
console.log("10 / 0 =", calc(10, 0, '/'));
console.log("10 ? 5 =", calc(10, 5, '?'));
