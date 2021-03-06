# -*- coding: utf-8 -*-
# Programación orientada a objetos
# Lección 4
# Herencia

import random
from Leccion_3 import Vector


class VectorRandomico(Vector):
    def __init__(self, rango_x=(0, 1), rango_y=(0, 1)):
        """ Construye un vector randómico """
        super().__init__()
        self.x = float(random.randrange(rango_x[0], rango_x[1]))
        self.y = float(random.randrange(rango_y[0], rango_y[1]))


def main():
    velocidad = VectorRandomico((0, 100), (0, 100))
    print(velocidad.magnitud())

    velocidad.sumar(VectorRandomico())
    velocidad.multiplicar(2.1)
    velocidad.normalizar()
    print(velocidad)

if __name__ == '__main__':
    main()
