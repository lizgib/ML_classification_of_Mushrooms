'''
parsing through the file julian got for us!
'''
import pandas as pd

ncbi = open('data/mushroom_toxicity.txt')
edible_bois = open('data/edible_bois.txt', 'r')
poison_bois = open('data/poison_bois.txt', 'r')
splist = open('data/spp_list.txt', 'r')
lines = splist.readlines()

consensus = {}
for l in lines:
    spp = l.strip()
    if spp not in consensus.keys():
        consensus[spp] = 1 # one is default (poisonous)

header = ncbi.readline()
lines = ncbi.readlines()
for l in lines:
    ll = l.strip().split('\t')
    spp = ll[0]
    ID = ll[3]
    if spp in consensus.keys():
        if ID == 'True':
            consensus[spp] = 1
        else:
            consensus[spp] = 0

lines = edible_bois.readlines()
for l in lines:
    spp = l.strip()
    if spp in consensus.keys():
        consensus[spp] = 0

lines = poison_bois.readlines()
for l in lines:
    spp = l.strip()
    if spp in consensus.keys():
        consensus[spp] = 1


pd.DataFrame.from_dict(data = consensus, orient = 'index').to_csv('data/consensus_IDS.txt', header = False, sep = '\t')
