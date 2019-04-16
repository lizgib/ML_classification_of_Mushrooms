import os

os.chdir('/Volumes/LIZGIB/shrooms/images')

spp_list = []
out = open('/Users/elizabethgibbons/Desktop/shrooms/spp_list.txt', 'w')
for f in os.listdir(os.getcwd()):
    spp = f.split('.')[0]
    if spp.find('TBD') != -1:
        pass
    else:
        out.write(spp)
        out.write('\n')
out.close()
