import math

def es_primo(num):
    """
    Determina si un número es primo.

    Un número primo es un número natural mayor que 1 que solo es divisible por 1 y por sí mismo.

    Parámetros:
        num (int o float): El número a evaluar. Si es un float equivalente a un entero, será convertido a entero.

    Retorna:
        bool: True si el número es primo, False en caso contrario.

    Excepciones:
        TypeError: Si el número no es un entero o un float equivalente a un entero.
    """
    # Convertir flotantes equivalentes a enteros
    if isinstance(num, float):
        if math.isclose(num, round(num)):
            num = int(round(num))
        else:
            raise TypeError("El número debe ser un entero")
    
    # Validar que la entrada sea un entero, pero excluir True y False
    if not isinstance(num, int) or isinstance(num, bool):
        raise TypeError("El número debe ser un entero")
    
    # Los números menores que 2 no son primos
    if num < 2:
        return False
    
    # Verificar divisibilidad solo hasta la raíz cuadrada de num
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    
    return True