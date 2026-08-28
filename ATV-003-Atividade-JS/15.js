// 15. Classe ContaBancaria
class ContaBancaria {
  constructor(titular, saldo = 0) {
    this.titular = titular;
    this.saldo = saldo;
  }

  depositar(valor) {
    this.saldo += valor;
    console.log(`[DEPOSITO] ${this.titular}: +R$ ${valor.toFixed(2)}`);
  }

  sacar(valor) {
    if (valor > this.saldo) {
      console.log(`[ERRO] ${this.titular}: saldo insuficiente para sacar R$ ${valor.toFixed(2)}! Saldo atual: R$ ${this.saldo.toFixed(2)}`);
      return false;
    }
    this.saldo -= valor;
    console.log(`[SAQUE] ${this.titular}: -R$ ${valor.toFixed(2)}`);
    return true;
  }

  extrato() {
    return `=== EXTRATO ===\nTitular: ${this.titular}\nSaldo  : R$ ${this.saldo.toFixed(2)}\n===============`;
  }
}

// Simulação de operações
let contaA = new ContaBancaria("Kellyson", 500);
let contaB = new ContaBancaria("Madruga", 50);

contaA.depositar(200);
contaA.sacar(100);
contaA.sacar(1000); // Erro de saldo

contaB.depositar(100);
contaB.sacar(120);

console.log("\n" + contaA.extrato());
console.log("\n" + contaB.extrato());
