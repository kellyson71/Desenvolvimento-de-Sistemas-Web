class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []
        
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
        
    def listar_alunos(self):
        print(f"--- Alunos de {self.nome} ---")
        for a in self.alunos:
            print(f"> {a.nome} ({a.matricula})")

c = Curso("Python Preguiçoso")
c.adicionar_aluno(Aluno("Jubileu", "111"))
c.adicionar_aluno(Aluno("Astolfo", "222"))
c.listar_alunos()
