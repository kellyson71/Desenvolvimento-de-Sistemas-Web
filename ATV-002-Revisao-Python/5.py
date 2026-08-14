class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.set_idade(idade)
        self.email = email
        
    def set_idade(self, valor):
        if valor < 0:
            print(f"Erro: idade negativa para {self.nome}! Zerando a idade.")
            self.__idade = 0
        else:
            self.__idade = valor
            
    def aniversario(self):
        self.__idade += 1
        
    def exibir_info(self):
        return f"Nome: {self.nome}, Idade: {self.__idade}, Email: {self.email}"

p = Pessoa("Chico", -5, "chico@email.com")
print(p.exibir_info())
p.aniversario()
print("Depois do aniversário:", p.exibir_info())
