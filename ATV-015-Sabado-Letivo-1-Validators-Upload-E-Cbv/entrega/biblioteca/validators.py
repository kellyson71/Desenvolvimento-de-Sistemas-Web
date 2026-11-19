from datetime import date

from django.core.exceptions import ValidationError

TAMANHO_MAXIMO_CAPA = 1024 * 1024


def validar_ano_publicacao(ano):
    ano_atual = date.today().year
    if ano < 1450 or ano > ano_atual:
        raise ValidationError(
            f"O ano precisa estar entre 1450 e {ano_atual}. Confira o ano de publicação do livro.",
            code="ano_invalido",
        )


def validar_tamanho_arquivo(arquivo):
    if arquivo.size > TAMANHO_MAXIMO_CAPA:
        tamanho_mb = arquivo.size / (1024 * 1024)
        raise ValidationError(
            f"A capa tem {tamanho_mb:.1f} MB e o limite é 1 MB. Escolha uma imagem menor.",
            code="arquivo_grande",
        )
