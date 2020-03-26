from random import *
from copy import *

def trzy_pierwsze_wartosci(lista, wp):
    indeksy = []
    wartosci = []
    licznik = 0
    for i in range(len(lista)):
        if lista[i] >= wp:
            indeksy.append(i)
            wartosci.append(lista[i])
            licznik += 1
        if licznik == 3:
            break

    return indeksy, wartosci

def sortowanie_1(lista,wp):
    indeksy, wartosci = trzy_pierwsze_wartosci(lista, wp)
    indeksy_wartosci = []
    index = []
    for k in range(len(indeksy)):
        indeksy_wartosci.append([indeksy[k],wartosci[k]])

    zakres = len(indeksy_wartosci) - 1
    for i in range(zakres):
        for j in range(zakres):
            if indeksy_wartosci[j+1][1] > indeksy_wartosci[j][1]:
                indeksy_wartosci[j+1], indeksy_wartosci[j] = indeksy_wartosci[j], indeksy_wartosci[j+1]

    for i in range(len(indeksy_wartosci)):
        index.append(indeksy_wartosci[i][0])

    return index

def sortowanie_2(lista,wp):
    indeksy, wartosci = trzy_pierwsze_wartosci(lista, wp)
    index = []
    while True:
        ind = wartosci.index(max(wartosci))
        index.append(indeksy[ind])
        wartosci.remove(wartosci[ind])
        indeksy.remove(indeksy[ind])
        if len(wartosci) == 0:
            break

    return index

lista = []
dlugosc_listy = 10
wartosc_progowa = 5
for i in range(dlugosc_listy):
    lista.append(randint(0, 10))
print("Dane: ", lista)
print("Wartość progowa: ", wartosc_progowa)
lista_1 = copy(lista)
lista_2 = copy(lista)
x = sortowanie_1(lista_1, wartosc_progowa)
y = sortowanie_2(lista_2, wartosc_progowa)
print("3 pierwsze indeksy posortowane sortowaniem 1: ", x)
print("3 pierwsze indeksy posortowane sortowaniem 2: ", y)