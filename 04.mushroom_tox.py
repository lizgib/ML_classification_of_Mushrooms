'''
parsing through the file julian got for us!
'''
import pandas as pd

ncbi = open('mushroom_toxicity.txt', 'r')
wikiIDS = open('poison_ids.txt', 'r')
header = ncbi.readline()
lines = ncbi.readlines()

consensus = {}
for l in lines:
    ll = l.strip().split('\t')
    spp = ll[0]
    ID = ll[3]
    if spp not in consensus.keys():
        consensus[spp] = 'NA'
    if ID == 'True':
        consensus[spp] = 1
    else:
        consensus[spp] = 0

header = wikiIDS.readline()
lines = wikiIDS.readlines()

for l in lines:
    ll = l.strip().split('\t')
    spp = ll[0]
    ID = ll[1]
    if spp in consensus.keys():
        if ID != 'NA':
            consensus[spp] = ID

pd.DataFrame.from_dict(data = consensus, orient = 'index').to_csv('consensus_IDS.txt', header = False, sep = '\t')
