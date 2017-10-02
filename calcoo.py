#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora:

    def __init__(self, valor1, valor2):
        self.v1 = valor1
        self.v2 = valor2

    def suma(self):
        return self.v1 + self.v2

    def resta(self):
        return self.v1 - self.v2


if __name__ == '__main__':
    try:
        valor1 = float(sys.argv[1])
        valor2 = float(sys.argv[3])
        objeto = Calculadora(valor1, valor2)
    except ValueError:
        sys.exit('Error: debe usar numeros')

    if sys.argv[2] == 'suma':
        resultado = objeto.suma()
    elif sys.argv[2] == 'resta':
        resultado = objeto.resta()
    else:
        sys.exit('Introducir: numero1 suma/resta numero2')
    print(resultado)
