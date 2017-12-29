import csv
import pprint
import math

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
osOz = 'oscar_nom'
osOx = 'want_fwb'
osOy = 'rate_fwb'

for key in slownikDane:
    rekordWartosci = [];
    wartosc = slownikDane[key];
    rekordWartosci.append(wartosc[osOx]);
    rekordWartosci.append(wartosc[osOy]);
    rekordWartosci.append(wartosc[osOz]);
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
elemZ = []
for lista in listaPunktow:
    elemX.append(lista[0])
    elemY.append(lista[1])
    elemZ.append(lista[2])


# *****************************************************
# pierwsza iteracja
# *****************************************************

# centroidy - budowa
import numpy as np
c1x = np.mean(elemX)
c1y = np.mean(elemY)
c1z = np.mean(elemZ)
c2x = np.mean(elemX) + np.mean(elemX)/2
c2y = np.mean(elemY) + np.mean(elemY)/2
c2z = np.mean(elemZ) + np.mean(elemZ)/2

#*********************************************************************
# budowa macierzy odleglosci
# ********************************************************************
macierzOdleglosci = [];
for lista in listaPunktow:
    row = []
    elX = lista[0]
    elY = lista[1]
    elZ = lista[2]
    odlC1 = math.sqrt(math.pow(c1x - elX, 2) + math.pow(c1y - elY, 2) + math.pow(c1z - elZ, 2))
    odlC2 = math.sqrt(math.pow(c2x - elX, 2) + math.pow(c2y - elY, 2) + math.pow(c2z - elZ, 2))
    row.append(odlC1);
    row.append(odlC2);
    macierzOdleglosci.append(row)


# *****************************************
# przyporzadkowanie punktow [grupowanie]
# *****************************************
pGrX = []
pGrY = []
pGrZ = []
dGrX = []
dGrY = []
dGrZ = []
licznik = 1;
slownikGrup = {}
pierwszaGrupa = 'pierwsza grupa'
drugaGrupa = 'druga grupa'
for row in macierzOdleglosci:
    e0 = row[0]
    e1 = row[1]
    if e0 <= e1:
        pGrX.append(slownikDane[licznik][osOx])
        pGrY.append(slownikDane[licznik][osOy])
        pGrZ.append(slownikDane[licznik][osOz])
        slownikGrup[slownikDane[licznik]['title']] = pierwszaGrupa
    else:
        dGrX.append(slownikDane[licznik][osOx])
        dGrY.append(slownikDane[licznik][osOy])
        dGrZ.append(slownikDane[licznik][osOz])
        slownikGrup[slownikDane[licznik]['title']] = drugaGrupa
    licznik = licznik + 1;

pprint.pprint(slownikGrup)

from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

fig = pyplot.figure()
ax = Axes3D(fig)
# print("aaaaaaaaa", pGrX)
# print("bbbbbbbbbbbb", pGrY)
# print("cccccccccc", pGrZ)

# ax.scatter(pGrX, pGrY, pGrZ, c = 'red')
# ax.scatter(dGrX, dGrY, dGrZ, c = 'green')
# ax.scatter(c1x, c1y, c1z, marker = '*', c = 'red', s = 250)
# ax.scatter(c2x, c2y, c2z, marker = '*', c = 'green', s = 250)
# ax.set_xlabel(osOx)
# ax.set_ylabel(osOy)
# ax.set_zlabel(osOz)
# pyplot.show()




# plt.scatter(pGrX, pGrY, c = 'red')
# plt.scatter(dGrX, dGrY, c = 'green')
# plt.scatter(c1x, c1y, c = '#9b0000', marker = '*', s = 250)
# plt.scatter(c2x, c2y, c = '#1c3900', marker = '*', s = 250)
# plt.show()
# # opis osi
# plt.ylabel(osOy)
# plt.xlabel(osOx)

#
# # ********************************************
# # druga iteracja
# # ********************************************
dC1X = np.mean(pGrX)
dC1Y = np.mean(pGrY)
dC1Z = np.mean(pGrZ)
dC2X = np.mean(dGrX)
dC2Y = np.mean(dGrY)
dC2Z = np.mean(dGrZ)

# ***********************************************
# budowa macierzy odleglosci
# ***********************************************
macierzOdleglosci2 = [];
for lista in listaPunktow:
    row = []
    elX = lista[0]
    elY = lista[1]
    elZ = lista[2]
    odlC1 = math.sqrt(math.pow(dC1X - elX, 2) + math.pow(dC1Y - elY, 2) + math.pow(dC1Z - elZ, 2))
    odlC2 = math.sqrt(math.pow(dC2X - elX, 2) + math.pow(dC2Y - elY, 2) + math.pow(dC2Z - elZ, 2))
    row.append(odlC1);
    row.append(odlC2);
    macierzOdleglosci2.append(row)

# ***********************************************
# grupowanie punktow
# ***********************************************

pGrX2 = []
pGrY2 = []
pGrZ2 = []
dGrX2 = []
dGrY2 = []
dGrZ2 = []
licznik2 = 1;

pierwszaGrupa = 'pierwsza grupa'
drugaGrupa = 'druga grupa'
liczbaPrzemieszczen = 0
for row in macierzOdleglosci2:
    e0 = row[0]
    e1 = row[1]
    if e0 <= e1:
        pGrX2.append(slownikDane[licznik2][osOx])
        pGrY2.append(slownikDane[licznik2][osOy])
        pGrZ2.append(slownikDane[licznik2][osOz])
        if slownikGrup[slownikDane[licznik2]['title']] != pierwszaGrupa:
            liczbaPrzemieszczen = liczbaPrzemieszczen + 1
            slownikGrup[slownikDane[licznik2]['title']] = pierwszaGrupa
        print("grupa pierwsza", slownikGrup[slownikDane[licznik2]['title']])
    else:
        dGrX2.append(slownikDane[licznik2][osOx])
        dGrY2.append(slownikDane[licznik2][osOy])
        dGrZ2.append(slownikDane[licznik2][osOz])
        if slownikGrup[slownikDane[licznik2]['title']] != drugaGrupa:
            liczbaPrzemieszczen = liczbaPrzemieszczen + 1
            slownikGrup[slownikDane[licznik2]['title']] = drugaGrupa
        print("grupa druga", slownikGrup[slownikDane[licznik2]['title']])
    licznik2 = licznik2 + 1;
print("Liczba przemieszczen: ", liczbaPrzemieszczen)


# ax.scatter(pGrX2, pGrY2, pGrZ2, c = 'red')
# ax.scatter(dGrX2, dGrY2, dGrZ2, c = 'green')
# ax.scatter(dC1X, dC1Y, dC1Z, marker = '*', c = 'black', s = 250)
# ax.scatter(dC2X, dC2Y, dC2Z, marker = '*', c = 'yellow', s = 250)
# ax.set_xlabel(osOx)
# ax.set_ylabel(osOy)
# ax.set_zlabel(osOz)
# pyplot.show()


# ************************************************************
# trzecia iteracja
# ************************************************************

tC1X = np.mean(pGrX2)
tC1Y = np.mean(pGrY2)
tC1Z = np.mean(pGrZ2)
tC2X = np.mean(dGrX2)
tC2Y = np.mean(dGrY2)
tC2Z = np.mean(dGrZ2)

# ***********************************************
# budowa macierzy odleglosci
# ***********************************************
macierzOdleglosci3 = [];
for lista in listaPunktow:
    row = []
    elX = lista[0]
    elY = lista[1]
    elZ = lista[2]
    odlC1 = math.sqrt(math.pow(tC1X - elX, 2) + math.pow(tC1Y - elY, 2) + math.pow(tC1Z - elZ, 2))
    odlC2 = math.sqrt(math.pow(tC2X - elX, 2) + math.pow(tC2Y - elY, 2) + + math.pow(tC2Z - elZ, 2))
    row.append(odlC1);
    row.append(odlC2);
    macierzOdleglosci3.append(row)

# ***********************************************
# grupowanie punktow
# ***********************************************

pGrX3 = []
pGrY3 = []
pGrZ3 = []
dGrX3 = []
dGrY3 = []
dGrZ3 = []
licznik3 = 1;

liczbaPrzemieszczen3 = 0
for row in macierzOdleglosci3:
    e0 = row[0]
    e1 = row[1]
    if e0 <= e1:
        pGrX3.append(slownikDane[licznik3][osOx])
        pGrY3.append(slownikDane[licznik3][osOy])
        pGrZ3.append(slownikDane[licznik3][osOz])
        if slownikGrup[slownikDane[licznik3]['title']] != pierwszaGrupa:
            liczbaPrzemieszczen3 = liczbaPrzemieszczen3 + 1
            slownikGrup[slownikDane[licznik3]['title']] = pierwszaGrupa
        print("grupa pierwsza", slownikGrup[slownikDane[licznik3]['title']])
    else:
        dGrX3.append(slownikDane[licznik3][osOx])
        dGrY3.append(slownikDane[licznik3][osOy])
        dGrZ3.append(slownikDane[licznik3][osOz])
        if slownikGrup[slownikDane[licznik3]['title']] != drugaGrupa:
            liczbaPrzemieszczen3 = liczbaPrzemieszczen3 + 1
            slownikGrup[slownikDane[licznik3]['title']] = drugaGrupa
        print("grupa druga", slownikGrup[slownikDane[licznik3]['title']])
    licznik3 = licznik3 + 1;
print("Liczba przemieszczen: ", liczbaPrzemieszczen3)

ax.scatter(pGrX3, pGrY3, pGrZ3, c = 'red')
ax.scatter(dGrX3, dGrY3, dGrZ3, c = 'green')
ax.scatter(tC1X, tC1Y, tC1Z, marker = '*', c = 'black', s = 250)
ax.scatter(tC2X, tC2Y, tC2Z, marker = '*', c = 'yellow', s = 250)
ax.set_xlabel(osOx)
ax.set_ylabel(osOy)
ax.set_zlabel(osOz)
pyplot.show()