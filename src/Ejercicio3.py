def limpiar_spoilers(texto_usuario):
    # Esta función separa las palabras spoiler ingresadas por coma
    # y elimina espacios extra
    partes = texto_usuario.split(",")
    spoilers = []

    for palabra in partes:
        palabra = palabra.strip()

        if palabra != "":
            spoilers.append(palabra)

    return spoilers


def reemplazar_una_palabra(texto, spoiler):
    # Esta función reemplaza una palabra spoiler por asteriscos
    # sin distinguir mayúsculas de minúsculas
    texto_minuscula = texto.lower()
    spoiler_minuscula = spoiler.lower()

    resultado = ""
    i = 0

    while i < len(texto):
        fragmento = texto_minuscula[i:i + len(spoiler)]

        if fragmento == spoiler_minuscula:
            resultado += "*" * len(spoiler)
            i += len(spoiler)
        else:
            resultado += texto[i]
            i += 1

    return resultado


def filtrar_spoilers(review, spoilers):
    # Esta función recorre la lista de spoilers
    # y los reemplaza uno por uno en el texto
    texto_filtrado = review

    for spoiler in spoilers:
        texto_filtrado = reemplazar_una_palabra(texto_filtrado, spoiler)

    return texto_filtrado