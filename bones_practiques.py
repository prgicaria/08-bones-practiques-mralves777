#!/usr/bin/env python
'''Divisió.py.Programa que demana dos nombres i els divideix.
Institut Icària
Programació - 1r Batxillerat - Curs 2025-26
El programa li demana al usuari el quocient i el divisor. La maquina
fa la operació matemàtica i en calcula el resultat de la divisió i
el residu
'''
__author__ = "Alejandro Mateo Alves Capiau"
__email__ = "aalves@instituticaria.cat"
__date__ = "2009/10/19"

Dividend = int(input("Ingresar dividend"))
Divisor = int(input("Ingresar divisor"))
Quocient = (Dividend)//(Divisor)
Residu = (Dividend) % (Divisor)
print(f"Divisió: {Dividend}/{Divisor}")
print(f"Quocient: {Quocient}")
print(f"Residu: {Residu}")
