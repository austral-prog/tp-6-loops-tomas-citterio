def power(base, exp):
    """
    Retorna base elevado a exp usando un bucle for.
    exp es siempre >= 0.

    Ejemplo: power(2, 3) -> 8  (2*2*2)
    """
    result = 1
    for _ in range(exp):
        result *= base
    return result


def sum_of_powers(base, max_exp):
    """
    Retorna la suma de base^0 + base^1 + ... + base^max_exp.
    Debe USAR la funcion power.

    Ejemplo: sum_of_powers(2, 3) -> 15  (1+2+4+8)
    """
    total = 0
    for exp in range(max_exp + 1):
        total += power(base, exp)
    return total
