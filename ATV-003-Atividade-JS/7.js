// 7. Pedra, Papel e Tesoura (sem repetir comparações)
function jokenpo(j1, j2) {
  j1 = j1.toLowerCase();
  j2 = j2.toLowerCase();

  if (j1 === j2) return "Empate";

  // Quem ganha de quem no jokenpo
  let ganhaDe = {
    pedra: "tesoura",
    tesoura: "papel",
    papel: "pedra"
  };

  return ganhaDe[j1] === j2 ? "Jogador 1 venceu!" : "Jogador 2 venceu!";
}

console.log("pedra vs tesoura ->", jokenpo("pedra", "tesoura"));
console.log("papel vs papel   ->", jokenpo("papel", "papel"));
console.log("tesoura vs pedra ->", jokenpo("tesoura", "pedra"));
