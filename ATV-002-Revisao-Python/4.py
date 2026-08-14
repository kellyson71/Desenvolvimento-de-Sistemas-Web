class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email
        
    def exibir_info(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Email: {self.email}"

p1 = Pessoa("João", 20, "joao@email.com")
p2 = Pessoa("Maria", 25, "maria@email.com")
p3 = Pessoa("José", 80, "jose@email.com")

print(p1.exibir_info())
print(p2.exibir_info())
print(p3.exibir_info())
