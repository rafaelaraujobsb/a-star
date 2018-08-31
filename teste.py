# -*- coding: utf-8 -*-
import heapq

matriz = (30, 30)
#matriz = (5, 5)
c = ''

# LINHA x COLUNA
m1 = [(i, 9) for i in range(20)]
m2 = [(i, 10) for i in range(20)]
m4 = [(9, i) for i in range(21,25)]
m3 = [(10, i) for i in range(21,25)]
m5 = [(i, 3) for i in range(10,30)]
m6 = [(20, i) for i in range(0,8)]
m7 = [(i, 24) for i in range(23,28)]
m8 = [(i, 24) for i in range(23,28)]
m9 = [(23, i) for i in range(23,27)]
m10 = [(i, 26) for i in range(23,28)]

muros = m1+m2+m4+m3+m5+m6+m7+m8+m9+m10
inicio = (0, 4)
destino = (25, 25)
#muros = [(1,1),(1, 2), (2, 2), (3, 2)]
#inicio = (2, 0)
#destino = (2, 4)



for x in range(matriz[0]):
    for y in range(matriz[1]):
        if (x, y) == inicio:
            c += 'C  '
        elif (x, y) == destino:
            c += 'M  '
        elif (x, y) in muros:
            c += '###'
            c = c.strip()
        else:
            c += '.  '

    c = c.strip()
    c += '\n'

print(c)


def in_area(vizinho):
    x, y = vizinho
    return  0 <= x < matriz[0] and 0 <= y < matriz[1]


def is_muro(vizinho):
    return vizinho not in muros

def vizinhos(atual):
    (x, y) = atual
    resultado = filter(in_area, [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]) # verifica se tá dentro da área
    resultado = filter(is_muro, resultado) # verifica se o vizinho não é um muro

    return resultado


def h(vizinho, destino):
    (x1, y1) = vizinho
    (x2, y2) = destino

    return abs(x1 - x2) + abs(y1 - y2)


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, custo, g, item):
        heapq.heappush(self.elements, (custo, g, item))

    def get(self):
        return heapq.heappop(self.elements)

lista_aberta = PriorityQueue()
caminho = {}
lista_fechada = {}

lista_aberta.put(0, 0, inicio)
lista_fechada[inicio] = 0

while not lista_aberta.empty():
    prioridade, distancia_inicio, atual = lista_aberta.get()

    if atual == destino:
        break

    for vizinho in vizinhos(atual):
        g = distancia_inicio + 1
        custo = g + h(vizinho, destino)

        if not vizinho in lista_fechada or g < lista_fechada[vizinho]:
            # Prioridade determinada por F = G + H (menor custo)
            lista_aberta.put(custo, g, vizinho)

            caminho[vizinho] = atual
            lista_fechada[vizinho] = g

# FILTRAR CAMINHOS
caminho_final = []
prox = caminho[destino]

while prox != inicio:
    caminho_final.append(prox)
    prox = caminho[prox]

c = ''
for x in range(matriz[0]):
    for y in range(matriz[1]):
        if (x, y) == inicio:
            c += 'C  '
        elif (x, y) == destino:
            c += 'M  '
        elif (x, y) in muros:
            c += '###'
            c = c.strip()
        elif (x, y) in caminho_final:
            c += '*  '
        else:
            c += '.  '

    c = c.strip()
    c += '\n'

print(c)
    