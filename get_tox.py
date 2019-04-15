import wikipedia
import requests
from bs4 import BeautifulSoup
import pandas as pd

html = requests.get('https://en.wikipedia.org/wiki/List_of_poisonous_fungus_species')
b = BeautifulSoup(html.text, 'lxml')
links = []

poison_bois = set()
out = open('poison_bois.txt', 'w')
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
ed = open('edible_bois.txt', 'r')
ed_lines = ed.readlines()
edible_bois = set()
for e in ed_lines:
    esp = e.strip()
    edible_bois.add(esp)

f = open('spp_list.txt', 'r')
lines = f.readlines()

spp_list = []
for l in lines:
    sp = l.strip()
    if sp.find('TBD') == -1:
        spp_list.append(sp)

id_dict = {}
how_many = 0
no_nas = {}
for sp in spp_list:
    if sp not in id_dict.keys():
        id_dict[sp] = 'NA'
    if sp not in no_nas.keys():
        no_nas[sp] = 1
    if sp in poison_bois:
        id_dict[sp] = 1
        no_nas[sp] = 1
        how_many += 1
    if sp in edible_bois:
        id_dict[sp] = 0
        no_nas[sp] = 0
        how_many +=1
print(how_many)
pd.DataFrame.from_dict(data=id_dict, orient='index').to_csv(('poison_ids.txt'), header=False, sep = '\t')
pd.DataFrame.from_dict(data=no_nas, orient='index').to_csv(('poison_ids_noNA.txt'), header=False, sep = '\t')
