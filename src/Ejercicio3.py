import re


def limpiar_spoilers(texto_usuario):
    # Esta función toma el texto ingresado por el usuario
    # y lo separa en una lista usando la coma.
    # También elimina espacios extra al inicio y al final.
    partes = texto_usuario.split(",")
    spoilers = []

    for palabra in partes:
        palabra = palabra.strip()

        if palabra != "":
            spoilers.append(palabra)

    return spoilers


def reemplazar_una_palabra(texto, palabra_spoiler):
    # Esta función reemplaza una palabra spoiler por asteriscos
    # sin importar si está en mayúscula o minúscula.
    asteriscos = "*" * len(palabra_spoiler)

    texto_modificado = re.sub(
        palabra_spoiler,
        asteriscos,
        texto,
        flags=re.IGNORECASE
    )

    return texto_modificado


def filtrar_spoilers(review, spoilers):
    # Esta función recorre toda la lista de spoilers
    # y los va reemplazando uno por uno en el texto.
    texto_filtrado = review

    for spoiler in spoilers:
        texto_filtrado = reemplazar_una_palabra(texto_filtrado, spoiler)

    return texto_filtrado