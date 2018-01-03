
import csv

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

liczbaTestowa = 5
import random
rekordyTest = random.sample(range(1, 100), 5)
print(rekordyTest)
slownikTest = {}

i = 1
for elem in rekordyTest:
    slownikTest[i] = slownikDane[elem]
    i = i + 1
print(slownikTest)

length = []
want_fwb = []
boxoffice = []
budget = []
votes_imdb = []

matrix = []
for key in slownikTest:
    matrixRekord = []
    rekord = slownikDane[key]
    matrixRekord.append(rekord['length'])
    matrixRekord.append(rekord['want_fwb'])
    matrixRekord.append(rekord['boxoffice'])
    matrixRekord.append(rekord['budget'])
    matrixRekord.append(rekord['votes_imdb'])
    matrix.append(matrixRekord)
print(matrix)

import numpy as np
corMatrix = np.corrcoef(matrix)
print(corMatrix)
import scipy as scipy
from scipy.linalg import eig
d = eig([[1]], [[0]])
print("oooooooooooo", d)
A = scipy.mat(corMatrix)
print("aaaaaa", A)
wartosciWlasne, vector = scipy.linalg.eig(A)
print("dddddddddddddd", wartosciWlasne)
print("vvvvvvvvvvvvvvvvv", vector)
# l1 , l2 , l3 = la
# print(l1 , l2 , l3)
# print(v [ : , 0])
# print(v [ : , 1 ])
# print(v [ : , 2 ])
