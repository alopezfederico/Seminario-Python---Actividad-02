def obtener_lineas(texto):
    # Esta función separa el texto en una lista de líneas
    lineas = texto.split(".")
    print(lineas)
    lineas_limpias = []

    for linea in lineas:
        print(linea)
        linea = linea.strip()
        if linea != "":
            lineas_limpias.append(linea)

    return lineas_limpias


def contar_palabras(linea):
    # Esta función cuenta cuántas palabras tiene una línea
    palabras = linea.split()
    return len(palabras)


def total_palabras(lineas):
    # Esta función suma la cantidad de palabras de todas las líneas
    total = 0

    for linea in lineas:
        total = total + contar_palabras(linea)

    return total


def mostrar_lineas_sobre_promedio(lineas, promedio):
    # Esta función muestra solo las líneas que tienen más palabras que el promedio
    print(f'Líneas por encima del promedio ({promedio:.2f} palabras):')

    for linea in lineas:
        cantidad = contar_palabras(linea)

        if cantidad > promedio:
            print(f' - "{linea}" ({cantidad} palabras)')