// 10. n-ésimo termo de Fibonacci (recursivo simples)
function fibonacci(n) {
  if (n <= 0) return 0;
  if (n === 1) return 1;
  return fibonacci(n - 1) + fibonacci(n - 2);
}

// 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
console.log("Termo 0 :", fibonacci(0));
console.log("Termo 1 :", fibonacci(1));
console.log("Termo 6 :", fibonacci(6));
console.log("Termo 7 :", fibonacci(7));
console.log("Termo 10:", fibonacci(10));
