// 11. Validação de senha
function validarSenha(senha) {
  let erros = [];

  if (senha.length < 8) {
    erros.push("Mínimo de 8 caracteres");
  }
  if (!/[A-Z]/.test(senha)) {
    erros.push("Ao menos uma letra maiúscula");
  }
  if (!/[0-9]/.test(senha)) {
    erros.push("Ao menos um número");
  }

  if (erros.length === 0) {
    return "Senha válida!";
  }
  return erros;
}

console.log("Teste '123':", validarSenha("123"));
console.log("Teste 'senhafraca':", validarSenha("senhafraca"));
console.log("Teste 'SenhaForte123':", validarSenha("SenhaForte123"));
