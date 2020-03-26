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
    index, wartosci = trzy_pierwsze_wartosci(lista, wp)
    zakres = len(wartosci) - 1
    for i in range(zakres):
        for j in range(zakres-i):
            if wartosci[j + 1] > wartosci[j]:
                wartosci[j + 1], wartosci[j] = wartosci[j], wartosci[j + 1]
                index[j + 1], index[j] = index[j], index[j + 1]

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
lista_1 = copy(lista)
lista_2 = copy(lista)
start = time.clock()
x = sortowanie_1(lista_1, wartosc_progowa)
stop = time.clock()
czas1 = stop - start
start = time.clock()
y = sortowanie_2(lista_2, wartosc_progowa)
stop = time.clock()
czas2 = stop - start
print("3 pierwsze indeksy (sortowanie 1): ", x, "czas: ", '%.7f' % czas1)
print("3 pierwsze indeksy (sortowanie 2): ", y, "czas: ", '%.7f' % czas2)
