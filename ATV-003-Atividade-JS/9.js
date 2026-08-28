// 9. Estatísticas das notas (média, maior e menor)
function resumoNotas(notas) {
  let soma = 0;
  for (let n of notas) soma += n;

  return {
    media: Number((soma / notas.length).toFixed(2)),
    maior: Math.max(...notas),
    menor: Math.min(...notas)
  };
}

let notasTurma = [7.5, 4.0, 9.2, 6.0, 8.5, 10.0, 3.5];
console.log(resumoNotas(notasTurma));
