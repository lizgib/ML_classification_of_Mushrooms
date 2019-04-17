'''
Get IDs from wikipedia table for poison species
poison species denoted with a 1
'''

import wikipedia
import requests
from bs4 import BeautifulSoup
import pandas as pd

html = requests.get('https://en.wikipedia.org/wiki/List_of_poisonous_fungus_species')
b = BeautifulSoup(html.text, 'lxml')
links = []

poison_bois = set()
out = open('data/poison_bois.txt', 'w')
for i in b.find_all(name = 'i'):
    # pull the actual link for each one
    for link in i.find_all('a', href=True):
        links.append(link['href'])
for l in links:
    if l.find('/wiki/') != -1:
        spp = l.split('/wiki/')[1]
        out.write(spp)
        out.write('\n')
        poison_bois.add(spp)


# looked at another table since there were not many IDs from the first one
html = requests.get('https://en.wikipedia.org/wiki/List_of_deadly_fungus_species')
b = BeautifulSoup(html.text, 'lxml')
links = []

for i in b.find_all(name = 'i'):
    # pull the actual link for each one
    for link in i.find_all('a', href=True):
        links.append(link['href'])
for l in links:
    if l.find('/wiki/') != -1:
        spp = l.split('/wiki/')[1]
        out.write(spp)
        out.write('\n')
        poison_bois.add(spp)

out.close()
