#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv

with open(sys.argv[1],newline='') as csvfile:
    operacionesreader = csv.reader(csvfile, delimiter =',')
    for operacion in operacionesreader:
        operador = operacion[0]  # suma, 1, 2, 3, 4, 5 -> suma
        resultado = int(operacion[1])  # suma, 1, 2, 3, 4, 5 -> 1 

        if operador == 'suma':
            for operando in operacion[2:]:
                resultado += int(operando)
        elif operador == 'resta':
            for operando in operacion[2:]:
                resultado -= int(operando)
        elif operador == 'multiplica':
            for operando in operacion[2:]:
                resultado *= int(operando)
        elif operador == 'divide':
            for operando in operacion[2:]:
                resultado /= int(operando)
        else:
            sys.exit('Entrada no admitida')
   
        print('el resultado de ', operador, 'es: ',resultado)
