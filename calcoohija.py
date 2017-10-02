#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo


class CalculadoraHija(calcoo.Calculadora):

    def mult(self):
        return self.v1 * self.v2

    def div(self):
        try:
            return self.v1 / self.v2
        except ZeroDivisionError:
            sys.exit('Division by zero is not allowed')

if __name__ == '__main__':
    try:
        valor1 = float(sys.argv[1])
        valor2 = float(sys.argv[3])
        objeto = CalculadoraHija(valor1, valor2)

    except ValueError:
        sys.exit('Error: debe usar numeros')
    except IndexError:
        sys.exit('python3 calcoohija.py operando1 operacion operando2')

    if sys.argv[2] == 'suma':
        resultado = objeto.suma()
    elif sys.argv[2] == 'resta':
        resultado = objeto.resta()
    elif sys.argv[2] == 'multiplica':
        resultado = objeto.mult()
    elif sys.argv[2] == 'divide':
            resultado = objeto.div()
    else:
        sys.exit('Introducir: operando1 operacion operando2')
    print(resultado)
