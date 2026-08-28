// 16. Classe Retângulo com área e perímetro
class Retangulo {
  constructor(base, altura) {
    this.base = base;
    this.altura = altura;
  }

  calcularArea() {
    return this.base * this.altura;
  }

  calcularPerimetro() {
    return 2 * (this.base + this.altura);
  }
}

let ret = new Retangulo(10, 5);
console.log("Base:", ret.base, "| Altura:", ret.altura);
console.log("Área:", ret.calcularArea());
console.log("Perímetro:", ret.calcularPerimetro());
