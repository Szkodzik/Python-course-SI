from random import *
from copy import *

def sortowanie_1(lista):
    zakres = len(lista) - 1
    for i in range(zakres):
        flaga = 1
        for j in range(zakres):
            if lista[j+1] < lista[j]:
                lista[j+1], lista[j] = lista[j], lista[j+1]
                flaga = 0
        if flaga == 1:
            break
    print("Sortowanie 1: ",lista)

def sortowanie_2(lista):
    lista_2 = []
    while True:
        index = lista.index(min(lista))
        lista_2.append(lista[index])
        lista.remove(lista[index])
        if len(lista) == 0:
            break
    print("sortowanie 2: ",lista_2)

lista = []
dlugosc_listy = 100
for i in range(dlugosc_listy):
    lista.append(randint(-100, 100))
print("Lista do sortowania: ",lista)
lista_1 = copy(lista)
lista_2 = copy(lista)
sortowanie_1(lista_1)
sortowanie_2(lista_2)
