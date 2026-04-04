def tiene_un_solo_arroba(email):
    # Esta función verifica que el email tenga exactamente un @
    return email.count("@") == 1


def tiene_texto_antes_del_arroba(email):
    # Esta función verifica que haya al menos un carácter antes del @
    partes = email.split("@")
    return len(partes[0]) > 0


def tiene_punto_despues_del_arroba(email):
    # Esta función verifica que después del @ haya al menos un punto
    partes = email.split("@")
    parte_despues = partes[1]
    return "." in parte_despues


def no_empieza_ni_termina_mal(email):
    # Esta función verifica que no empiece ni termine con @
    # y tampoco con dos puntos seguidos
    if email.startswith("@") or email.endswith("@"):
        return False

    if email.startswith("..") or email.endswith(".."):
        return False

    return True


def dominio_valido(email):
    # Esta función verifica que después del último punto
    # haya al menos 2 caracteres
    ultimo_punto = email.rfind(".")

    if ultimo_punto == -1:
        return False

    parte_final = email[ultimo_punto + 1:]

    return len(parte_final) >= 2


def email_valido(email):
    # Esta función junta todas las validaciones
    if not tiene_un_solo_arroba(email):
        return False

    if not tiene_texto_antes_del_arroba(email):
        return False

    if not tiene_punto_despues_del_arroba(email):
        return False

    if not no_empieza_ni_termina_mal(email):
        return False

    if not dominio_valido(email):
        return False

    return True