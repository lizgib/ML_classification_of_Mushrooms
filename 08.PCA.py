#Import the data from scikit-learn
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pickle
import time

from image_processing import label_img, load_training_data, get_vectors, get_labels

DIR = os.getcwd()+'/test_imgs'

feature_vectors, class_labels = get_vectors()
labels = get_labels()

feature_vectors,class_labels = np.array(feature_vectors),np.array(class_labels)

categories = labels.keys()
n_samples = 905
n_features = 905
h = 64 #pixel height
w = 64 #pixel width
n_classes = len(categories)

train_vectors, test_vectors, train_labels, test_labels = train_test_split(feature_vectors, class_labels, random_state=1, test_size=0.25)

print('Amount of training vectors: {}'.format(len(train_vectors)))
print('Amount of testing vectors: {}'.format(len(test_vectors)),'\n')

 # This is much less than the original n_features

print("Extracting the top {}% eigenfaces from {} faces".format(99, train_vectors.shape[0]))

#Set up the pca object with the number of compoents we want to find
pca = PCA(svd_solver = 'full',n_components=.99, whiten=True)

#Fit the training data to the pca model.
_ = pca.fit(train_vectors)

pca_train_vectors = pca.transform(train_vectors)
pca_test_vectors = pca.transform(test_vectors)

print("Training set changed from a size of: ", train_vectors.shape, ' to: ', pca_train_vectors.shape)
print("Testing set changed from a size of: ", test_vectors.shape, ' to: ', pca_test_vectors.shape)

n_components = pca_test_vectors.shape[1]

plt.figure(figsize = (20,15))
plt.plot(pca.explained_variance_ratio_, marker="o")
plt.title('\"Best\" Feature Vectors')
plt.ylabel('Feature Vector Weight')
plt.xlabel('Eigenfaces')
plt.show()

total_variance = np.sum(pca.explained_variance_ratio_)*100
print("These %d eigenvectors account for a total of %d percent of the total variance in the original dataset"
      % (n_components, total_variance))

start = time.time()
rerun_training = True
filename = os.getcwd()+'ShroomsPCA.p'
# make some temporary variables so you can change this easily
tmp_vectors = pca_train_vectors
tmp_labels = train_labels

# Train a SVM classification model  NOTE This can take ~ 5 minutes or more!!!!

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

################################################################################
#Predicting

predict_vectors = pca_test_vectors
true_labels = test_labels
print("Predicting mushroom toxicity on the test set")
pred_labels = clf.predict(predict_vectors)

print(classification_report(true_labels, pred_labels))
