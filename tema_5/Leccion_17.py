# -*- coding: utf-8 -*-
# Herramientas para computación científica
# Lección 17
# SymPy: Cálculo diferencial e integral

from sympy import *


def main():
    x = symbols("x")

    fx = sin(x) * exp(x)
    print(limit(fx, x, 0))
    print(diff(fx, x))

    fx = sin(x ** 2)
    print(integrate(fx, (x, -oo, oo)))

    fx = 1 / cos(x)
    print(series(fx, x))

    fx = cos(x) ** 2
    print(latex(Integral(fx, (x, 0, pi))))

if __name__ == '__main__':
    main()
