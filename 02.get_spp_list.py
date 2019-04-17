'''
go through the image names in the image directory to get species names
'''

import os

os.chdir('/Resized_shrooms')
# should be 866 images in the Resized_shrooms dir, so there should be 866 labels in the spp_list
spp_list = []
out = open('../data/spp_list.txt', 'w')
for f in os.listdir(os.getcwd()):
    spp = f.split('.')[0]
    if spp.find('TBD') != -1: # skip all TBD species. if they don't have an ID for us we can't tell if its poison
        pass
    else:
        out.write(spp)
        out.write('\n')
out.close()
