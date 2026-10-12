def a_binario(n):
    return format(n, "b")


def a_hexadecimal(n):
    return format(n, "x")


def a_entero(texto):
    try:
        return int(texto)
    except ValueError:
        print("El texto no es un número entero válido.")
        return None