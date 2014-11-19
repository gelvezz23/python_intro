# Introduccion al lenguaje de programacion Python
# Leccion 3
# Estructuras de control de flujo - while


def obtener_sucesion_fibonacci(n):
    """ Imprime todos los x pertenecientes a la sucesion de Fibonacci
        tales que x > n 
    """
    a = 0
    x = 1
    while x < n:
        print(x)
        a, x = x, a + x
