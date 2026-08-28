// 4. Ano de nascimento, voto e serviço militar
let anoNasc = 2008;
let anoAtual = new Date().getFullYear();
let idade = anoAtual - anoNasc;

let podeVotar = idade >= 16;
let votoObrigatorio = idade >= 18 && idade < 70;
let isentoMilitar = idade < 18 || idade > 45;

console.log("Idade:", idade);
console.log("Pode votar?", podeVotar ? "Sim" : "Não");
console.log("Voto obrigatório?", votoObrigatorio ? "Sim" : "Não");
console.log("Isento do serviço militar?", isentoMilitar ? "Sim" : "Não (precisa se alistar!)");
