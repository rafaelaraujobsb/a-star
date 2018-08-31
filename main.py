# -*- coding: utf-8 -*-
from a_star import a_star, Area

x, y = input('Digite o tamanho da matriz LxC: ').split('x')
matriz = (x, y)

origem = eval(input('Digite a cordenada de origem (X,Y): '))
destino = eval(input('Digite a cordenada do destino (X,Y): '))

matriz = Area(origem, destino, matriz)

print(matriz.mostrar_area())

print()

a_star(matriz)
