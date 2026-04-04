def convertir_a_segundos(duration):
    # Recibo una duración en formato "m:ss" y la convierte a segundos
    partes = duration.split(":")
    minutos = int(partes[0])
    segundos = int(partes[1])

    total_segundos = minutos * 60 + segundos
    return total_segundos


def convertir_a_minutos_segundos(total_segundos):
    # Recibo una cantidad total de segundos y la convierte a formato "Xm Ys"
    minutos = total_segundos // 60
    segundos = total_segundos % 60

    return f"{minutos}m {segundos}s"


def calcular_duracion_total(playlist):
    # Sumo la duración de todas las canciones
    total_segundos = 0

    for song in playlist:
        total_segundos += convertir_a_segundos(song["duration"])

    return total_segundos


def buscar_cancion_mas_larga(playlist):
    # Busco la canción con mayor duración
    cancion_mas_larga = playlist[0]
    mayor_duracion = convertir_a_segundos(playlist[0]["duration"])

    for song in playlist:
        duracion_actual = convertir_a_segundos(song["duration"])

        if duracion_actual > mayor_duracion:
            mayor_duracion = duracion_actual
            cancion_mas_larga = song

    return cancion_mas_larga


def buscar_cancion_mas_corta(playlist):
    # Busco la canción con menor duración
    cancion_mas_corta = playlist[0]
    menor_duracion = convertir_a_segundos(playlist[0]["duration"])

    for song in playlist:
        duracion_actual = convertir_a_segundos(song["duration"])

        if duracion_actual < menor_duracion:
            menor_duracion = duracion_actual
            cancion_mas_corta = song

    return cancion_mas_corta