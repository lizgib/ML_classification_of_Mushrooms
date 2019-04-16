import wikipedia
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Poison Species

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
