#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv
import calcoohija

try:
    with open(sys.argv[1],) as csvfile:  # abrir fichero
        operacionesreader = csv.reader(csvfile)  # leer fichero
        for operacion in operacionesreader:
            try:
                operador = operacion[0]  # suma, 1, 2, 3, 4, 5 -> suma
                resultado = float(operacion[1])  # suma, 1, 2, 3, 4, 5 -> 1

                for operando in operacion[2:]:
                    num = float(operando)
                    objeto = calcoohija.CalculadoraHija(resultado, num)

                    if operador == 'suma':
                        resultado = objeto.suma()
                    elif operador == 'resta':
                        resultado = objeto.resta()
                    elif operador == 'multiplica':
                        resultado = objeto.mult()
                    elif operador == 'divide':
                        resultado = objeto.div()
                    else:
                        sys.exit('operacion,num,num...')
                print(resultado)

            except ValueError:
                sys.exit('Error: debe usar numeros')
except IndexError:
    sys.exit('python3 calcoohija.py <fichero.csv>')
