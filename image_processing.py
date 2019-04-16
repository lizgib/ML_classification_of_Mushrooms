from PIL import Image
import numpy as np
import os
from random import shuffle
import matplotlib.pyplot as plt
import pandas as pd

#DIR = '/Volumes/LIZGIB/shrooms/images'
DIR = '/Users/elizabethgibbons/Desktop/shrooms/ML_classification_of_Mushrooms/Resized_shrooms'

def get_labels():
    '''
    Grab the labels for each species based on premade key
    '''
    label_file = open('/Users/elizabethgibbons/Desktop/shrooms/ML_classification_of_Mushrooms/data/consensus_IDS.txt')
    lines = label_file.readlines()
    labels = {}
    for l in lines:
        ll = l.strip().split('\t')
        if ll[0] not in labels.keys():
            labels[ll[0]] = ll[1]
    return labels


def label_img(name, labels):
    '''
    Get the ID for that a species
    '''
    return labels[name]

IMG_SIZE = 300
def load_training_data(labels):
    '''
    load each image into an array. All these images go into one big array with their labels
    '''
    train_data = []
    for img in os.listdir(DIR):
        name = img.split('.')[0]
        label = label_img(name, labels)
        path = os.path.join(DIR, img)
        if "DS_Store" not in path:
            img = Image.open(path)
            img = img.convert('L')
            img = img.resize((IMG_SIZE, IMG_SIZE), Image.ANTIALIAS)
            train_data.append([np.array(img), label])
    shuffle(train_data)
    return train_data

def get_vectors():
    '''
    unpacks the arrays into class_labels and feature_vectors that will work with
    our model. Making this kinda resemble the sklearn datasets we worked with in
    class
    '''
    labels = get_labels()
    train_data = load_training_data(labels)
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
    return feature_vectors, class_labels
get_vectors()
