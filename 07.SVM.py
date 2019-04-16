#Import the data from scikit-learn
from PIL import Image
import numpy as np
import os
from random import shuffle
import matplotlib.pyplot as plt
from image_processing import label_img, load_training_data, get_vectors, get_labels
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pickle
import time
#DIR = '/Volumes/LIZGIB/shrooms/images'
DIR = '/Users/elizabethgibbons/Desktop/shrooms/ML_classification-of-Mushrooms/Resized_shrooms'

feature_vectors, class_labels = get_vectors()
labels = get_labels()

categories = labels.keys()
n_samples = 905
n_features = 905
N = 507
h = 64
w = 64
n_classes = len(categories)


import matplotlib.pylab as plt
from ipywidgets import interact


train_vectors, test_vectors, train_labels, test_labels = train_test_split(feature_vectors, class_labels, random_state=1, test_size=0.25)

print(len(train_vectors))
print(len(test_vectors))


filename = '/Users/elizabethgibbons/Desktop/shrooms/ML-classification-of-grains/SVM_out'
rerun_training = True

# Train a SVM classification model  NOTE This can take ~ 5 minutes or more!!!!


# make some temporary variables so you can change this easily
tmp_vectors = train_vectors
tmp_labels = train_labels


start = time.time()
if rerun_training:
    print("Fitting the classifier to the training set")
    param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5],
                  'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1], }
    clf = GridSearchCV(SVC(kernel='rbf', class_weight='balanced'), param_grid)
    clf = clf.fit(tmp_vectors, tmp_labels)
    # print("Best estimator found by grid search:")
    # print(clf.best_estimator_)
    #save the model to a file
    # pickle.dump(clf, open(filename, 'wb'))

# else:
    #read the model from a file
    # print("reading pickle file.")
    # clf = pickle.load(open(filename, 'rb'))
    # print("Best estimator found by grid search:")
    # print(clf.best_estimator_)

end = time.time()
print("Runtime",end - start)

################################################################################
# Visualization part from the notebook


predict_vectors = test_vectors
true_labels = test_labels
print(test_labels)
print("Predicting people's names on the test set")
pred_labels = clf.predict(predict_vectors)

print(classification_report(true_labels, pred_labels))
print(confusion_matrix(true_labels, pred_labels, labels=range(n_classes)))

def plot_gallery(images, true_titles, pred_titles, h, w, n_row=5, n_col=5):
    """Helper function to plot a gallery of portraits"""
    plt.figure(figsize=(1.8 * n_col, 2.4 * n_row))
    plt.subplots_adjust(bottom=0, left=.01, right=.99, top=.90, hspace=.35)
    for i in range(n_row * n_col):
        plt.subplot(n_row, n_col, i + 1)
        plt.imshow(images[i].reshape((h, w)), cmap=plt.cm.gray)
        plt.title('Pred='+str(categories[pred_titles[i]]), size=9)
        plt.xlabel('Actual='+str(categories[true_titles[i]]), size=9)
        plt.xticks(())
        plt.yticks(())

plot_gallery(test_vectors, test_labels, pred_labels, h,w)
