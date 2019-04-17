# ML-classification-of-grains
Project directory for CMSE 202 semester project


### Introduction
----------------
  Mushrooms are prized as a food source, and as such are not only cultivated but foraged for in the wild. However, wild mushroom foraging can come with considerable risk, as many mushrooms are toxic and inedible to humans. While extensive lists of mushrooms and their properties exist in various places, this information is scattered and sometimes hard to obtain, however many modern foragers will have access to a smartphone with the ability to take pictures and access the internet. With this in mind we wondered if there is a way to leverage modern computational techniques to ease the burden of mushroom foragers by using images matched to webscraped data about toxicity to classify mushrooms as either poisionous or edible.  

Here we investigated the question: Can machine learning be used to classify mushrooms as being either edible or poisonous based on their images alone?

-To investigate this, we used three techniques common to machine learning, principal component analysis, a support vector machine, and a convolutional nueral network.These were then trained using image data obtained from online databases and species and toxicity/edibility information gathered using several web scrapping packages.

-Below one can find information on the libraries and packages used, instructions on how to run the relevant code, details about group member contributions, as well as references used. 
### Contents
-------------
1. `00.get_images.py`: download all the images from http://mushroom.pro
2. `01.Resizing_data.ipynb`: make all images same size for ML models 
3. `02.get_spp_list.py`: go through the image names in the image directory to get species names
4. `03.spp_query_from_julian.py`: webscraper from Julian Liber which queries species names to ncbi and records
instances of identifying keywords
5. `03.EdibleMushrooms.py`: edible mushroom IDs from wikipedia 
6. `03.get_tox.py`: poison mushroom IDs from wikipedia
7. `04.mushroom_tox.py`: combine all poision Ids into master dataframe for labels 
8. `image_processing05.py`: load and format images to be ready for ML models 
9. `06.SVM_mushrooms.ipynb`: run SVM and plot precision recall 
10. `08.PCA.py`: Runs a PCA model for our mushroom data
11. `CNN-Final.ipynb`: run CNN 
12. `VisualizeFinalScript.ipynb`: get visuals from CNN


### List of included libraries
-------------------------------
#### Tensor Flow
  - Keras
  
#### Requests
  - get
  
#### bs4
  - BeautifulSoup
  
#### os
  - chdir
  - listdir
  
#### urllib 

#### pandas 
  - from_dict
  - to_csv
  
#### numpy 

#### selenium 
  - webdriver 
  
#### sklearn
  - svm 
  - metrics 
  - model_selection
  - PCA
  
### Instructions
----------------
-CNN: To use the CNN, simply open and run every cell in the jupyter notebook file 'CNN-Final.ipynb'. The only specific action needed by the user is to specify the directory path to where the folder 'Resized-shrooms' and the text files 'posion_ids_noNA.txt' and 'poision_ids' reside, as they contain the relevant images and labels. Inside the script 'CNN-Final' there are two cells with comments in the upper right corner (cells 2 and 3) which say "User Action Needed". In cell 3 lines 2 and 3 must have the paths called by open() set to the location of 'Resized-shrooms' and 'poision_ids.txt' respectively, and in cell 2 line 3, the path called by open() must be set to wherever 'poision_ids_noNa.txt' is.

-PCA: Run the python script in ML_classification_of_Mushrooms folder downloaded from github. As long as `08.PCA.py` has not been moved, no directory path needs to be decalred (due to `os.getcwd()`). The script will pause about halfway through when a .png image is displayed. Once this image has been closed the script will continue to run until the prediction summary is printed as an output. Note: there will be a couple of warning due to package versions and inaccuracy.

-SVM: Load in data using image_processing05.py. Run SVM using sklearn as was done in class Day 18. Plots precision and recall. Output is written to SVM_out pickle file (not pushed)  

### Group Contributions 
----------------
Michael: CNN code, and code to visualize intermediate layer output

Lizzie: SVM, image_processing05.py, image downloads and webscraping, poison IDs

Luke: PCA, webscraping, nonpoison IDs, image reduction

### Resources
---------------

1)G. P. (2018, November 02). Visualizing intermediate activation in Convolutional Neural Networks with Keras. Retrieved from https://towardsdatascience.com/visualizing-intermediate-activation-in-convolutional-neural-networks-with-keras-260b36d60d0

2)Train a simple deep CNN on the CIFAR10 small images dataset. (n.d.). Retrieved from https://keras.io/examples/cifar10_cnn/

3)https://github.com/gabrielpierobon/cnnshapes/blob/master/README.md

4) images from: https://www.mushroom.pro/db/aa-index.php

5) poison IDs from: https://en.wikipedia.org/wiki/List_of_poisonous_fungus_species and https://en.wikipedia.org/wiki/List_of_deadly_fungus_species

6) edible IDs from: https://en.wikipedia.org/wiki/Category:Edible_fungi

7) image_processing05.py adapted from: https://towardsdatascience.com/image-classification-python-keras-tutorial-kaggle-challenge-45a6332a58b8

8) SVM from in class day 18: https://github.com/msu-cmse-courses/cmse202-S19-assignments/blob/master/Day-18/Day-18_In-Class_MachineLearningPCA-STUDENT.ipynb

9) the rest of the image IDs were obtained from NCBI with the help of Julian Liber (specified in scripts) 

