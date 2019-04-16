import requests
from bs4 import BeautifulSoup
import csv

htmls = ['https://en.wikipedia.org/wiki/Category:Edible_fungi',
        'https://en.wikipedia.org/w/index.php?title=Category:Edible_fungi&pagefrom=Lactarius+glyciosmus%0ALactarius+glyciosmus#mw-pages',
        'https://en.wikipedia.org/w/index.php?title=Category:Edible_fungi&pagefrom=Suillus+punctipes#mw-pages']
edible_bois = []
page = 1

append_true = ['Agaricus_abruptibulbus','Lactarius_glyciosmus','Suillus_punctipes']
append_false = ['Lactarius_fragilis','Xeromphalina_campanella','Suillus_pseudobrevipes']
for html in htmls:
    page += 1
    html = requests.get(html)
    b = BeautifulSoup(html.text, 'lxml')

    append = False
    links = []
    for i in b.find_all(name = 'li'):
        # pull the actual link for each one
        for link in i.find_all('a', href=True):
            links.append(link['href'])
    for l in links:
        if l.find('/wiki/') != -1:
            spp = l.split('/wiki/')[1]
            if spp in append_true:
                append = True
            if append:
                edible_bois.append(spp)
            if spp in append_false:
                append = False


out = open('data/edible_bois.txt', 'w')

for shroom in edible_bois:
    out.write(shroom)
    out.write('\n')

out.close()
