from PIL import Image
import numpy as np
import os
from random import shuffle
import matplotlib.pyplot as plt
import pandas as pd

#DIR = '/Volumes/LIZGIB/shrooms/images'
DIR = '/Users/elizabethgibbons/Desktop/shrooms/ML-classification-of-grains/Resized_shrooms'


# specify the file you want to get your labels from
label_file = open('/Users/elizabethgibbons/Desktop/shrooms/ML-classification-of-grains/poison_ids_NAdel.txt')
lines = label_file.readlines()
labels = {}
for l in lines:
    ll = l.strip().split('\t')
    if ll[0] not in labels.keys():
        labels[ll[0]] = ll[1]

def label_img(name):
    return labels[name]

IMG_SIZE = 300
def load_training_data():
    train_data = []
    for img in os.listdir(DIR):
        name = img.split('.')[0]
        try:
            label = label_img(name)
            path = os.path.join(DIR, img)
            if "DS_Store" not in path:
                img = Image.open(path)
                img = img.convert('L')
                img = img.resize((IMG_SIZE, IMG_SIZE), Image.ANTIALIAS)
                train_data.append([np.array(img), label])
        except:
            print('%s not included in poison_ids label file chosen' %name)

    shuffle(train_data)
    return train_data


def main():
    train_data = load_training_data()
    feature_vectors = []
    class_labels = []
    for i in train_data:
        for j in i:
            try:
                j.shape
                ar = j.flatten()
                feature_vectors.append(ar)
            except:
                class_labels.append(j)
    print(len(feature_vectors))
    print(len(class_labels))
main()
