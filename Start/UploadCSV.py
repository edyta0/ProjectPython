import pandas as pandas

data = pandas.read_csv('C:/Users/edyta/Desktop/ProjectPython/csfa.csv', encoding='cp1252');
print(data);

budget = (data[['budget']]);
print(budget);
length = (data[['length']]);
print(length);
