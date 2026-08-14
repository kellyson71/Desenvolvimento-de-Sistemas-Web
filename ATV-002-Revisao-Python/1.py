#1

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

maior = None

menor = None

media = None

def func():
    global maior, menor, media
    maior = max(lista)
    menor = min(lista)
    media = sum(lista) / len(lista)

    print("Maior número:", maior)
    print("Menor número:", menor)
    print("Média:", media)

func()

