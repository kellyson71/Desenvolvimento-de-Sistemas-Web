// 6. Classificação de IMC
function classificarIMC(peso, altura) {
  let imc = peso / (altura * altura);
  if (imc < 18.5) return "Abaixo do peso";
  if (imc < 25) return "Normal";
  if (imc < 30) return "Sobrepeso";
  return "Obesidade";
}

console.log("70kg e 1.75m:", classificarIMC(70, 1.75));
console.log("50kg e 1.75m:", classificarIMC(50, 1.75));
console.log("85kg e 1.75m:", classificarIMC(85, 1.75));
console.log("110kg e 1.75m:", classificarIMC(110, 1.75));
