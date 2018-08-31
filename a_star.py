# -*- coding: utf-8 -*-
import heapq
from random import randint
import colorama
from colorama import Fore, Back, Style

from pprint import pprint

class PriorityQueue:
    def __init__(self):
        self.elements = []


    def empty(self) -> bool:
        return len(self.elements) == 0


    def put(self, custo, g, item):
        heapq.heappush(self.elements, (custo, g, item))


    def get(self) -> tuple:
        return heapq.heappop(self.elements)


class Area:
    def __init__(self, origem: tuple, destino: tuple, matriz: tuple):
        self.linha = int(matriz[0])
        self.coluna = int(matriz[1])
        self.origem = origem
        self.destino = destino
        self.muros = []
        self.gerar_muro()


    def mostrar_area(self, caminho = []) -> str:
        c = ''
        for x in range(self.linha):
            for y in range(self.coluna):
                if (x, y) == self.origem:
                    c += Fore.YELLOW + 'C  ' + Style.RESET_ALL
                elif (x, y) == self.destino:
                    c += Fore.GREEN + 'M  ' + Style.RESET_ALL
                elif (x, y) in self.muros:
                    c += Fore.LIGHTCYAN_EX + '###' + Style.RESET_ALL
                    c = c.strip()
                elif (x, y) in caminho:
                    colorama.init()
                    c += Fore.RED + '*  ' + Style.RESET_ALL
                else:
                    c += '.  '

            c = c.strip()
            c += '\n'

        return c


    def gerar_muro(self):
        tam = int(self.linha * self.coluna * 0.40)

        for _ in range(tam):
            self.muros.append(randint(0,self.linha))

        for i in range(tam):
            x = self.muros[i]
            y = randint(0,self.coluna)

            self.muros[i] = (x, y)

        try: 
            self.muros.remove(self.destino)
        except:
            pass
        
        try:
            self.muros.remove(self.origem)   
        except:
            pass


    def in_area(self, coordenada: tuple) -> bool:
        x, y = coordenada
        
        return  0 <= x < self.linha and 0 <= y < self.coluna

    
    def is_muro(self, coordenada: tuple) -> bool:
        return coordenada not in self.muros


    def vizinhos(self, coordenada: tuple) -> list:
        x, y = coordenada
        resultado = filter(self.in_area, [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]) # verifica se tá dentro da área
        resultado = filter(self.is_muro, resultado) # verifica se o vizinho não é um muro

        return resultado


    def h(self, vizinho: tuple) -> int:
        x1, y1 = vizinho
        x2, y2 = self.destino

        return abs(x1 - x2) + abs(y1 - y2)


def a_star(matriz: Area):
    lista_aberta = PriorityQueue()
    lista_fechada = {}
    caminho = {}

    lista_aberta.put(0, 0, matriz.origem)
    lista_fechada[matriz.origem] = 0

    while not lista_aberta.empty():
        distancia_inicio, atual = lista_aberta.get()[1:]

        if atual == matriz.destino:
            break

        for vizinho in matriz.vizinhos(atual):
            g = distancia_inicio + 1
            custo = g + matriz.h(vizinho)

            if not vizinho in lista_fechada or g < lista_fechada[vizinho]:
                # Prioridade determinada por F = G + H (menor custo)
                lista_aberta.put(custo, g, vizinho)

                caminho[vizinho] = atual
                lista_fechada[vizinho] = g
    
    # Filtrar caminho
    caminho_final = []

    try:
        prox = caminho[matriz.destino]

        while prox != matriz.origem:
            caminho_final.append(prox)
            prox = caminho[prox]

        print(matriz.mostrar_area(caminho_final))
    except KeyError:
        print(matriz.mostrar_area())
        # print(caminho[matriz.origem])
        raise Exception('Não foi possível encontrar a rota!')
        #print()
