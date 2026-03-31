def crear_tabla_inicial(rounds):
    # Armo la tabla inicial de participantes. Todos los valores iniciados en 0
    tabla = {}

    '''
    Los participantes se extraen directamente del diccionario rounds.
    Sus nombres son el elemento en la posición 0, 

    '''
    participantes = rounds[0]['scores'].keys()

    for participante in participantes:
        tabla[participante] = {
            'puntaje_total': 0,
            'rondas_ganadas': 0,
            'mejor_ronda': 0,
        }

    return tabla


def calcular_puntaje_participante(scores_jueces):
    # Esta función suma los 3 puntajes de un participante en una ronda
    total = 0

    for puntaje in scores_jueces.values():
        total += puntaje

    return total


def obtener_tabla_ordenada(tabla):
    # función que convierte el diccionario en lista y la ordena por puntaje total
    lista_tabla = list(tabla.items())
    lista_tabla.sort(key=criterio_orden, reverse=True)
    return lista_tabla


def criterio_orden(item):
    # función para ordenar por puntaje total
    return item[1]['puntaje_total']


def mostrar_tabla(tabla,  rounds):
    
    # Imprime la tabla por pantalla

    tabla_ordenada = obtener_tabla_ordenada(tabla)

    print('{:^15} {:^15} {:^18} {:^15} {:^10}'.format(
    'Cocinero',
    'Puntaje total',
    'Rondas ganadas',
    'Mejor ronda',
    'Promedio'
))
    print('-'*80)
    for nombre, datos in tabla_ordenada:
        promedio = datos['puntaje_total'] / len(rounds)
        
        print('{:^15} {:^15} {:^18} {:^15} {:^10}'.format(
            nombre,
            datos['puntaje_total'],
            datos['rondas_ganadas'],
            datos['mejor_ronda'],
            round(promedio, 1)
            )
        )   


def procesar_ronda(ronda, tabla):
    # Esta función procesa una sola ronda:
    # calcula puntajes, actualiza la tabla y devuelve el ganador de la ronda
    
    puntajes_ronda = {} # Almacenar para cada participante el puntaje total de la ronda

    for participante, scores_jueces in ronda['scores'].items():
        puntaje = calcular_puntaje_participante(scores_jueces)
        puntajes_ronda[participante] = puntaje

        tabla[participante]['puntaje_total'] += puntaje

        if puntaje > tabla[participante]['mejor_ronda']:
            tabla[participante]['mejor_ronda'] = puntaje

    ganador = ''
    mejor_puntaje = -1

    for participante, puntaje in puntajes_ronda.items():
        if puntaje > mejor_puntaje:
            mejor_puntaje = puntaje
            ganador = participante

    tabla[ganador]['rondas_ganadas'] += 1

    return ganador, mejor_puntaje

