def palindromo_o_capicua(dato):
    if isinstance(dato, int):
        dato_str = str(dato)
        if dato_str == dato_str[::-1]:
            return True
        else:
            return False
    else:
        dato = dato.replace(" ", "").lower()
        if dato == dato[::-1]:
            return True
        else:
            return False
