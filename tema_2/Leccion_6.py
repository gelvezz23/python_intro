# -*- coding: utf-8 -*-
# Introducción al lenguaje de programacion Python
# Lección 6
# Accediendo a los valores de una lista

fibonacci = [1, 1, 2, 3, 4, 5, 8, 13, 21, 34]

print(fibonacci[0])
print(fibonacci[-1])
print(fibonacci[3:])
print(fibonacci[:3])
print(fibonacci[2:7])
print(fibonacci[2:7:2])

fibonacci[3:6] = []
print(fibonacci)

copia = fibonacci[:]
print(id(fibonacci), id(copia))

copia.reverse()
print(copia, fibonacci)
