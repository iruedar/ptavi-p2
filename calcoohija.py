#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, calcoo

class CalculadoraHija(calcoo.Calculadora):

    def mult(self):
        return valor1 * valor2

    def div(self):
        return valor1 / valor2

if __name__=='__main__':
    try:
        valor1 = int(sys.argv[1])
        valor2 = int(sys.argv[3])
        objeto = CalculadoraHija(valor1,valor2)
        if int(sys.argv[3]) == 0:
            sys.exit('La división entre cero no está permitida')
    except ValueError:
        sys.exit('Error: debe usar números')
  
    if sys.argv[2] == 'suma':
        resultado = objeto.suma()
    elif sys.argv[2] == 'resta':
        resultado = objeto.resta()
    elif sys.argv[2] == 'multiplica':
        resultado = objeto.mult()
    elif sys.argv[2] == 'divide':
        resultado = objeto.div()
    else:
        sys.exit('La operación debe ser suma, resta, multiplica o divide')
    print('El resultado es:', resultado)
