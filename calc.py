#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def suma(op1, op2):
    return op1 + op2


def resta(op1, op2):
    return op1 - op2

if __name__ == "__main__":
    try:
        valor1 = int(sys.argv[1])
        valor2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        resultado = suma(operando1, operando2)
    elif sys.argv[2] == "resta":
        resultado = resta(operando1, operando2)
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print(resultado)
