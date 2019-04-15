#Import the data from scikit-learn
from PIL import Image
import numpy as np
import os
from random import shuffle
import matplotlib.pyplot as plt

#DIR = '/Volumes/LIZGIB/shrooms/images'
DIR = '/Users/elizabethgibbons/Desktop/shrooms/ML-classification-of-grains/Resized_shrooms'
# label_file = open('/Users/elizabethgibbons/Desktop/shrooms/ML-classification-of-grains/poison_ids_noNA.txt')
# lines = label_file.readlines()
# labels = {}
# for l in lines:
#     ll = l.strip().split('\t')
#     if ll[0] not in labels.keys():
#         labels[ll[0]] = ll[1]
#
# def label_present(name):
#     if name in labels.keys():
#         return True
#     else:
#         return False
#
#
# def label_img(name):
#     return labels[name]
#
# IMG_SIZE = 300
# def load_training_data():
#     train_data = []
#     for img in os.listdir(DIR):
#         name = img.split('.')[0]
#         if label_present(name):
#             label = label_img(name)
#             path = os.path.join(DIR, img)
#             if "DS_Store" not in path:
#                 img = Image.open(path)
#                 img = img.convert('L')
#                 img = img.resize((IMG_SIZE, IMG_SIZE), Image.ANTIALIAS)
#                 train_data.append([np.array(img), label])
#
#     shuffle(train_data)
#     return train_data
#
# train_data = load_training_data()
# # need to load in the images 50/50 poisonous/nonpoisonous
#
# feature_vectors = []
# class_labels = []
# for i in train_data:
#     for j in i:
#         try:
#             j.shape
#             ar = j.flatten()
#             feature_vectors.append(ar)
#         except:
#             class_labels.append(j)
# print(feature_vectors)
# print(class_labels)

# feature_vectors = np.array([i[0] for i in train_data]).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
# class_labels = np.array([i[1] for i in train_data])
categories = labels.keys()
n_samples = 905
n_features = 905
print(n_samples, n_features)
N = 507
h = 64
w = 64
n_classes = len(categories)


import matplotlib.pylab as plt
from ipywidgets import interact



from sklearn.model_selection import train_test_split
# Note, if you have an older version of scikit-learn,
# you might need to replace the above line with the one below
#from sklearn.cross_validation import train_test_split

train_vectors, test_vectors, train_labels, test_labels = train_test_split(feature_vectors, class_labels, random_state=1, test_size=0.25)

print(len(train_vectors))
print(len(test_vectors))


filename = '/Users/elizabethgibbons/Desktop/shrooms/ML-classification-of-grains/SVM_out'
rerun_training = True

# Train a SVM classification model  NOTE This can take ~ 5 minutes or more!!!!
from sklearn.model_selection import GridSearchCV
# If you have an old version of sklearn that you have upgraded yet,
# you will need to change the above import to the one below
# from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC
import pickle
import time

#make some temporary variables so you can change this easily
tmp_vectors = train_vectors
tmp_labels = train_labels


start = time.time()
if rerun_training:
    print("Fitting the classifier to the training set")
    param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5],
                  'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1], }
    clf = GridSearchCV(SVC(kernel='rbf', class_weight='balanced'), param_grid)
    clf = clf.fit(tmp_vectors, tmp_labels)
    print("Best estimator found by grid search:")
    print(clf.best_estimator_)
    #save the model to a file
    pickle.dump(clf, open(filename, 'wb'))

else:
    #read the model from a file
    print("reading pickle file.")
    clf = pickle.load(open(filename, 'rb'))
    print("Best estimator found by grid search:")
    print(clf.best_estimator_)

end = time.time()
print("Runtime",end - start)
