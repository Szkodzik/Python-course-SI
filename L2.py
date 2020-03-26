from random import *
from copy import *
import time

def trzy_pierwsze_wartosci(lista, wp):
    indeksy = []
    wartosci = []
    licznik = 0
    for i in range(len(lista)):
        if lista[i] > wp:
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
dlugosc_listy = 100
wartosc_progowa = 6
for i in range(dlugosc_listy):
    lista.append(round(uniform(-10, 10),2))
print("Dane: ", lista)
print("Wartość progowa: ", wartosc_progowa)
start = time.clock()
lista_1 = copy(lista)
stop = time.clock()
czas1 = stop - start
start = time.clock()
lista_2 = copy(lista)
stop = time.clock()
czas2 = stop - start
x = sortowanie_1(lista_1, wartosc_progowa)
y = sortowanie_2(lista_2, wartosc_progowa)
print("3 pierwsze indeksy (sortowanie 1): ", x, "czas: ", '%.7f' % czas1)
print("3 pierwsze indeksy (sortowanie 2): ", y, "czas: ", '%.7f' % czas2)
