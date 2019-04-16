import os

os.chdir('/Users/elizabethgibbons/Desktop/shrooms/ML_classification_of_Mushrooms/Resized_shrooms')
# should be 866 images in the Resized_shrooms dir, so there should be 866 labels in the spp_list
spp_list = []
out = open('/Users/elizabethgibbons/Desktop/shrooms/ML_classification_of_Mushrooms/data/spp_list.txt', 'w')
for f in os.listdir(os.getcwd()):
    spp = f.split('.')[0]
    if spp.find('TBD') != -1:
        pass
    else:
        out.write(spp)
        out.write('\n')
out.close()
