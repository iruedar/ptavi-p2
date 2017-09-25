#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class Calculadora:

    def __init__(self, valor1, valor2):
        self.v1 = valor1
        self.v2 = valor2

    def suma (self):
        return self.v1 + self.v2

    def resta (self):
        return self.v1 + self.v2


if __name__=='__main__':
    try:
        valor1 = int(sys.argv[1])
        valor2 = int(sys.argv[3])
        objeto = Calculadora(valor1,valor2)
    except ValueError:
        sys.exit('Error: debe usar números')
  
    if sys.argv[2] == 'suma':
        resultado = objeto.suma()
    elif sys.argv[2] == 'resta':
        resultado = objeto.resta()
    else:
        sys.exit('La operación debe ser suma o resta')
    print('El resultado es:', resultado)
