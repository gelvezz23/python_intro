# -*- coding: utf-8 -*-
# Programación orientada a objetos
# Lección 2
# Constructor

import math


class Vector(object):
    """ Vector de 2D """

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

if __name__ == '__main__':
    velocidad = Vector()
    print(velocidad.x, velocidad.y)

    aceleracion = Vector(2, 0.4)
    aceleracion.x = 1.4
    print(aceleracion.x, aceleracion.y)
