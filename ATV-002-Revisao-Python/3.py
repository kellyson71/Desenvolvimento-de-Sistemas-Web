nomes = ["Ana", "Bruno", "Carlos", "Ana", "Bruno", "Ana"]

contagem = {}
for n in nomes:
    contagem[n] = contagem.get(n, 0) + 1

print("Contagem:", contagem)

repetidos = list(set([n for n in nomes if nomes.count(n) > 1]))
print("Repetidos:", repetidos)
