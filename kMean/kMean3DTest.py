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

slownik = {};
i = 1;
with open('baza.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         slownik[i] = {'title' : row['title'],
                       'genre' : row['genre'],
                       'country' : row['country'],
                       'premiere' : int(row['premiere']),
                       'premiere_pl' : int(row['premiere_pl']),
                       'genre' : row['genre'],
                       'length' : int(row['length']),
                       'rate_fwb' : float(row['rate_fwb']),
                       'votes_fwb' : float(row['votes_fwb']),
                       'want_fwb' : float(row['want_fwb']),
                       'boxoffice' : float(row['boxoffice']),
                       'budget' : float(row['budget']),
                       'gross_usa' : row['gross_usa'],
                       'rate_imdb' : float(row['rate_imdb']),
                       'votes_imdb' : row['votes_imdb'],
                       'oscar_nom' : float(row['oscar_nom']),
                       'oscar_won' : float(row['oscar_won']),
                       'rasp_nom' : float(row['rasp_nom']),
                       'rasp_won' : float(row['rasp_won']),
                       'gold_nom' : float(row['gold_nom']),
                       'gold_won' : float(row['gold_won']),
                       'gga' : float(row['gga']),
                       'bafta' : float(row['bafta'])
                       };
         i = i + 1;
pprint.pprint(slownik);

listaPunktow = [];
for key in slownik:
    malaLista = [];
    wartosc = slownik[key];
	# tutaj sobie zmien wartosci na oskach
	# os ox
    malaLista.append(wartosc['budget']);
	# os oy
    malaLista.append(wartosc['want_fwb']);
    # dochodzi os oz
    malaLista.append(wartosc['oscar_won']);
    listaPunktow.append(malaLista);

print(randint(0, 9))
# *********************************************************************
# szukamy maksymalnych punktow
xMax = listaPunktow[0][0];
yMax = listaPunktow[0][1];
zMax = listaPunktow[0][2];

print("cccccccccccccccccc", xMax)
print("cccccccccccccccccc", yMax)

# for lista in listaPunktow:
#     elementX = lista[0]
#     if elementX > xMax:
#         xMax = elementX
#     elementY = lista[1]
#     if elementY > xMax:
#         xMax = elementY

elemX = []
elemY = []
elemZ = []
for lista in listaPunktow:
    elemX.append(lista[0])
    elemY.append(lista[1])
    elemZ.append(listaPunktow[2])

import numpy as np
meanElemX1 = np.mean(elemX)
meanElemY1 = np.mean(elemY)
meanElemZ1 = np.mean(elemZ)

import statistics
meanElemX2 = np.mean(elemX) + 30
meanElemY2 = np.mean(elemY) + 30
meanElemZ2 = np.mean(elemZ) + 30


print("xxxxxxxxxxxxxxx", xMax)
print("xxxxxxxxxxxxxxx", yMax)

# *********************************************************************
# ustawiamy srodki dla centroidow
import random
c1x = meanElemX1#20#random.uniform(0, xMax);
c1y = meanElemY1#20#random.uniform(0, yMax);
c2x = meanElemX2#10#random.uniform(0, xMax);
c2y = meanElemY2#10#random.uniform(0, yMax);
c1z = meanElemZ1#30#random.uniform(0, yMax);
c2z = meanElemZ2#30#random.uniform(0, yMax);
print("ddddddddd", c1x, c1y, c2x, c2y);

#*********************************************************************
# budowa macierzy odleglosci
macierzOdleglosci = [];
for lista in listaPunktow:
    row = []
    elX = lista[0]
    elY = lista[1]
    elZ = lista[2]
    odlC1 = math.sqrt(math.pow(c1x - elX, 2) + math.pow(c1y - elY, 2) + math.pow(c1z - elZ, 2))
    print("ppppppp ", odlC1)
    odlC2 = math.sqrt(math.pow(c2x - elX, 2) + math.pow(c2y - elY, 2) + math.pow(c2z - elZ, 2))
    row.append(odlC1);
    row.append(odlC2);
    macierzOdleglosci.append(row)

print("wwwwwwwwwwwwww", macierzOdleglosci)

# *************************************************************************
# budowa wykresow

listaX = []
listaY = []
listaZ = []
for lista in listaPunktow:
    wspX = lista[0]
    listaX.append(wspX)
    wspY = lista[1]
    listaY.append(wspY)
    wspZ = lista[2]
    listaZ.append(wspZ)

centrX = [c1x, c2x]
centrY = [c1y, c2y]
centrZ = [c1z, c2z]
plt.scatter(listaX, listaY)
plt.scatter(centrX, centrY, c = 'red')
# opis osi
plt.ylabel('budget')
plt.xlabel('budget')
#plt.show()


pGrX = []
pGrY = []
pGrZ = []
dGrX = []
dGrY = []
dGrZ = []

licznik = 1
for row in macierzOdleglosci:
    e0 = row[0]
    e1 = row[1]
    if e0 <= e1:
        pGrX.append(slownik[licznik]['budget'])
        pGrY.append(slownik[licznik]['want_fwb'])
        pGrZ.append(slownik[licznik]['oscar_won'])
    else:
        dGrX.append(slownik[licznik]['budget'])
        dGrY.append(slownik[licznik]['want_fwb'])
        dGrZ.append(slownik[licznik]['oscar_won'])
    licznik = licznik + 1;




from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

fig = pyplot.figure()
ax = Axes3D(fig)

print(pGrX, pGrY, pGrZ, "aaaaaaaaaaaaaaaaaaaaa")

ax.scatter(pGrX, pGrY, pGrZ, c = 'red')
ax.scatter(dGrX, dGrY, dGrZ, c = 'green')
ax.scatter(c1x, c1y, c1z, marker = '*', c = 'red', s = 50 )
ax.scatter(c2x, c2y, c2z, marker = '*', c = 'green', s = 50 )
ax.set_xlabel('budget')
ax.set_ylabel('want_fwb')
ax.set_zlabel('oscar_won')
pyplot.show()







print("zzzzzzzzzzzzzzzzz", listaPunktow[0][0])