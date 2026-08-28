// 8. Palíndromo ignorando maiúsculas/minúsculas e espaços
function ehPalindromo(str) {
  let limpo = str.toLowerCase().replaceAll(" ", "");
  let invertido = limpo.split("").reverse().join("");
  return limpo === invertido;
}

console.log("A cara rajada da jararaca ->", ehPalindromo("A cara rajada da jararaca"));
console.log("Socorram me subi no onibus em Marrocos ->", ehPalindromo("Socorram me subi no onibus em Marrocos"));
console.log("Javascript ->", ehPalindromo("Javascript"));
