class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email
        
    def exibir_info(self):
        return f"Nome: {self.nome} | Idade: {self.idade} | Email: {self.email}"

class Aluno(Pessoa):
    def __init__(self, nome, idade, email, matricula, curso):
        super().__init__(nome, idade, email)
        self.matricula = matricula
        self.curso = curso
        
    def exibir_dados_aluno(self):
        return f"{self.exibir_info()} | Matrícula: {self.matricula} | Curso: {self.curso}"

a1 = Aluno("Cleiton", 22, "cleitin@grau.com", "2023001", "Engenharia de Gambiarras")
print(a1.exibir_dados_aluno())
