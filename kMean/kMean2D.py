import csv
import pprint
import math
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import itertools
from random import randint
import matplotlib.pyplot as plt
# ****************************************************
# przygotowanie danych jako mapa i lista punktow
# ****************************************************
slownikDane = {};
i = 1;
with open('baza.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         slownikDane[i] = {'title' : row['title'],
                       'country' : row['country'],
                       'premiere' : int(row['premiere']),
                       'premiere_pl' : int(row['premiere_pl']),
                       'genre' : row['genre'],
                       'length' : int(row['length']),
                       'rate_fwb' : float(row['rate_fwb']),
                       'votes_fwb' : float(row['votes_fwb']),
                       'want_fwb' : float(row['want_fwb']),
                       'boxoffice' : int(row['boxoffice']),
                       'budget' : int(row['budget']),
                       'gross_usa' : int(row['gross_usa']),
                       'rate_imdb' : float(row['rate_imdb']),
                       'votes_imdb' : float(row['votes_imdb']),
                       'oscar_nom' : int(row['oscar_nom']),
                       'oscar_won' : int(row['oscar_won']),
                       'rasp_nom' : int(row['rasp_nom']),
                       'rasp_won' : int(row['rasp_won']),
                       'gold_nom' : int(row['gold_nom']),
                       'gold_won' : int(row['gold_won']),
                       'gga' : int(row['gga']),
                       'bafta' : int(row['bafta'])
                       };
         i = i + 1;
# pprint.pprint(slownikDane);

listaPunktow = [];
osOx = 'budget'
osOy = 'want_fwb'

for key in slownikDane:
    rekordWartosci = [];
    wartosc = slownikDane[key];
    rekordWartosci.append(wartosc[osOx]);
    rekordWartosci.append(wartosc[osOy]);
    listaPunktow.append(rekordWartosci);

# *********************************************************************
# # szukamy maksymalnych punktow
# xMax = listaPunktow[0][0];
# yMax = listaPunktow[0][1];
#
# print("cccccccccccccccccc", xMax)
# print("cccccccccccccccccc", yMax)
#
# for lista in listaPunktow:
#     elementX = lista[0]
#     if elementX > xMax:
#         xMax = elementX
#     elementY = lista[1]
#     if elementY > xMax:
#         xMax = elementY
#
# print("xxxxxxxxxxxxxxx", xMax)
# print("xxxxxxxxxxxxxxx", yMax)

# *********************************************************************
# ustawiamy srodki dla centroidow
# import random
# c1x = random.uniform(0, xMax);
# c1y = random.uniform(0, yMax);
# c2x = random.uniform(0, xMax);
# c2y = random.uniform(0, yMax);
# print("ddddddddd", c1x, c1y, c2x, c2y);

# podzial punktow na x i y
elemX = []
elemY = []
for lista in listaPunktow:
    elemX.append(lista[0])
    elemY.append(lista[1])


# *****************************************************
# pierwsza iteracja
# *****************************************************

# centroidy - budowa
import numpy as np
c1x = np.mean(elemX)
c1y = np.mean(elemY)
c2x = np.mean(elemX) + np.mean(elemX)/2
c2y = np.mean(elemY) + np.mean(elemY)/2

#*********************************************************************
# budowa macierzy odleglosci
# ********************************************************************
macierzOdleglosci = [];
for lista in listaPunktow:
    row = []
    elX = lista[0]
    elY = lista[1]
    odlC1 = math.sqrt(math.pow(c1x - elX, 2) + math.pow(c1y - elY, 2))
    odlC2 = math.sqrt(math.pow(c2x - elX, 2) + math.pow(c2y - elY, 2))
    row.append(odlC1);
    row.append(odlC2);
    macierzOdleglosci.append(row)


# *****************************************
# przyporzadkowanie punktow [grupowanie]
# *****************************************
pGrX = []
pGrY = []
dGrX = []
dGrY = []
licznik = 1;
slownikGrup = {}
pierwszaGrupa = 'pierwsza grupa'
drugaGrupa = 'druga grupa'
for row in macierzOdleglosci:
    e0 = row[0]
    e1 = row[1]
    if e0 <= e1:
        pGrX.append(slownikDane[licznik]['budget'])
        pGrY.append(slownikDane[licznik]['want_fwb'])
        slownikGrup[slownikDane[licznik]['title']] = pierwszaGrupa
    else:
        dGrX.append(slownikDane[licznik]['budget'])
        dGrY.append(slownikDane[licznik]['want_fwb'])
        slownikGrup[slownikDane[licznik]['title']] = drugaGrupa
    licznik = licznik + 1;

pprint.pprint(slownikGrup)


plt.scatter(pGrX, pGrY, c = 'red')
plt.scatter(dGrX, dGrY, c = 'green')
plt.scatter(c1x, c1y, c = '#9b0000', marker = '*', s = 250)
plt.scatter(c2x, c2y, c = '#1c3900', marker = '*', s = 250)
plt.show()
# opis osi
plt.ylabel(osOy)
plt.xlabel(osOx)


# ********************************************
# druga iteracja
# ********************************************
dC1X = np.mean(pGrX)
dC1Y = np.mean(pGrY)
dC2X = np.mean(dGrX)
dC2Y = np.mean(dGrY)

# ***********************************************
# budowa macierzy odleglosci
# ***********************************************
macierzOdleglosci2 = [];
for lista in listaPunktow:
    row = []
    elX = lista[0]
    elY = lista[1]
    odlC1 = math.sqrt(math.pow(dC1X - elX, 2) + math.pow(dC1Y - elY, 2))
    odlC2 = math.sqrt(math.pow(dC2X - elX, 2) + math.pow(dC2Y - elY, 2))
    row.append(odlC1);
    row.append(odlC2);
    macierzOdleglosci2.append(row)

# ***********************************************
# grupowanie punktow
# ***********************************************

pGrX2 = []
pGrY2 = []
dGrX2 = []
dGrY2 = []
licznik2 = 1;

pierwszaGrupa = 'pierwsza grupa'
drugaGrupa = 'druga grupa'
liczbaPrzemieszczen = 0
for row in macierzOdleglosci2:
    e0 = row[0]
    e1 = row[1]
    if e0 <= e1:
        pGrX2.append(slownikDane[licznik2]['budget'])
        pGrY2.append(slownikDane[licznik2]['want_fwb'])
        if slownikGrup[slownikDane[licznik2]['title']] != pierwszaGrupa:
            liczbaPrzemieszczen = liczbaPrzemieszczen + 1
            slownikGrup[slownikDane[licznik2]['title']] = pierwszaGrupa
        print("grupa pierwsza", slownikGrup[slownikDane[licznik2]['title']])
    else:
        dGrX2.append(slownikDane[licznik2]['budget'])
        dGrY2.append(slownikDane[licznik2]['want_fwb'])
        if slownikGrup[slownikDane[licznik2]['title']] != drugaGrupa:
            liczbaPrzemieszczen = liczbaPrzemieszczen + 1
            slownikGrup[slownikDane[licznik2]['title']] = drugaGrupa
        print("grupa druga", slownikGrup[slownikDane[licznik2]['title']])
    licznik2 = licznik2 + 1;
print("Liczba przemieszczen: ", liczbaPrzemieszczen)

plt.scatter(pGrX2, pGrY2, c = 'red')
plt.scatter(dGrX2, dGrY2, c = 'green')
plt.scatter(dC1X, dC1Y, c = '#9b0000', marker = '*', s = 250)
plt.scatter(dC2X, dC2Y, c = '#1c3900', marker = '*', s = 250)
plt.ylabel(osOy)
plt.xlabel(osOx)
plt.show()

# ************************************************************
# trzecia iteracja
# ************************************************************

tC1X = np.mean(pGrX2)
tC1Y = np.mean(pGrY2)
tC2X = np.mean(dGrX2)
tC2Y = np.mean(dGrY2)

# ***********************************************
# budowa macierzy odleglosci
# ***********************************************
macierzOdleglosci3 = [];
for lista in listaPunktow:
    row = []
    elX = lista[0]
    elY = lista[1]
    odlC1 = math.sqrt(math.pow(tC1X - elX, 2) + math.pow(tC1Y - elY, 2))
    odlC2 = math.sqrt(math.pow(tC2X - elX, 2) + math.pow(tC2Y - elY, 2))
    row.append(odlC1);
    row.append(odlC2);
    macierzOdleglosci3.append(row)

# ***********************************************
# grupowanie punktow
# ***********************************************

pGrX3 = []
pGrY3 = []
dGrX3 = []
dGrY3 = []
licznik3 = 1;

liczbaPrzemieszczen3 = 0
for row in macierzOdleglosci3:
    e0 = row[0]
    e1 = row[1]
    if e0 <= e1:
        pGrX3.append(slownikDane[licznik3]['budget'])
        pGrY3.append(slownikDane[licznik3]['want_fwb'])
        if slownikGrup[slownikDane[licznik3]['title']] != pierwszaGrupa:
            liczbaPrzemieszczen3 = liczbaPrzemieszczen3 + 1
            slownikGrup[slownikDane[licznik3]['title']] = pierwszaGrupa
        print("grupa pierwsza", slownikGrup[slownikDane[licznik3]['title']])
    else:
        dGrX3.append(slownikDane[licznik3]['budget'])
        dGrY3.append(slownikDane[licznik3]['want_fwb'])
        if slownikGrup[slownikDane[licznik3]['title']] != drugaGrupa:
            liczbaPrzemieszczen3 = liczbaPrzemieszczen3 + 1
            slownikGrup[slownikDane[licznik3]['title']] = drugaGrupa
        print("grupa druga", slownikGrup[slownikDane[licznik3]['title']])
    licznik3 = licznik3 + 1;
print("Liczba przemieszczen: ", liczbaPrzemieszczen3)

plt.scatter(pGrX3, pGrY3, c = 'red')
plt.scatter(dGrX3, dGrY3, c = 'green')
plt.scatter(tC1X, tC1Y, c = '#9b0000', marker = '*', s = 250)
plt.scatter(tC2X, tC2Y, c = '#1c3900', marker = '*', s = 250)
plt.ylabel(osOy)
plt.xlabel(osOx)
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
ax.set_xticks([0., 0.5, 1.])
plt.show()


