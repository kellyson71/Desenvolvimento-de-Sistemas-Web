# 2

texto = "testo de teste para atividade de desenvolvimento de web"

def func(texto):
    vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    contagem = 0
    for letra in texto:
        if letra in vogais:
            contagem += 1

    print("Número de vogais:", contagem)

    texto_invertido = texto[::-1]
    print("Texto invertido:", texto_invertido)

    palindromo = texto.replace(" ", "").lower() == texto.replace(" ", "").lower()[::-1]
    print("É palíndromo?", palindromo)

func(texto)