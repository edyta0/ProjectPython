import csv
import pprint

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
                       'votes_fwb' : row['votes_fwb'],
                       'want_fwb' : row['want_fwb'],
                       'boxoffice' : row['boxoffice'],
                       'budget' : row['budget'],
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