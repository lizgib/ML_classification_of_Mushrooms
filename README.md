# ML-classification-of-grains
Project directory for CMSE 202 semester project


### Introduction
----------------
*** Add intro ***
(Feel free to edit any of this/delete my notes)
(Not sure what the tone of of this is supposed to be like, so I sorta added a story-esque first paragraph, if this is not appropriate it can be deleted and i think it still makes sense)
Mushrooms are prized as a food source, and as such are not only cultivated but foraged for in the wild. However, wild mushroom foraging can comes with considerable risk because many mushrooms are toxic and inedible to humans. While extensive lists of mushrooms and there properties exist in various places, this information is scattered and sometimes hard to obtain, however many modern foragers will have access to a smartphone with the ability to take pictures and access the internet. With this in mind we wondered if there is a way to leverage modern computational techniques to ease the burden of mushroom foragers by using images matched to webscraped data about toxicity to classify mushrooms as either poisionous or edible.  

Here we investigated the question: Can Machine Learning be used to classify mushrooms as being either edible or poisionous based on their images alone?

-to investigate this, we used three techniques common to machine learning, principal component analysis, a support vector machine, and a convolutional nerual network.These were then trained using image data obtained from online databases and species and toxicity/edibility information gathered using several web scrapping packages.

-Below one can find information on the libraries and packages used, instructions on how to run the relevant code, details about group member contributions, as well as references used. 
### Contents
-------------
1. `CNN-For-Group.ipynb`: Convolutional Neural Network
2. `Edible_Mushrooms.py`: Web Scraping for Edible Mushrooms script
3. `edible_bois.txt`: List of edible mushrooms (results from `Edible_Mushrooms.py`)
4. `get_images.py`: Extracting data from 
5. `get_spp_list.py`: Extracting mushroom species from data
6. `get_tox.py`: Web Scraping for toxic mushrooms script
7. `poison_bois.txt`: List of toxic Mushrooms (results from `get_tox.py`)
8. `poison_ids.txt`: Mushrooms species and their toxic/edible label
9. `spp_list.txt`: List of mushroom species from data


### List of included libraries
-------------------------------
#### Tensor Flow
  - Sequential
  - Load_data
  - Dense
  - Flatten
  - MaxPool2d
  - Compile
  
#### Requests
  - get
  
#### bs4
  - BeautifulSoup
  
#### os
  - chdir
  - listdir
  
### Instructions
----------------

### Group Contributions 
----------------
Michael- CNN code, and code to visualize intermediate layer output

### Resources
---------------

1)G. P. (2018, November 02). Visualizing intermediate activation in Convolutional Neural Networks with Keras. Retrieved from https://towardsdatascience.com/visualizing-intermediate-activation-in-convolutional-neural-networks-with-keras-260b36d60d0

2)Train a simple deep CNN on the CIFAR10 small images dataset. (n.d.). Retrieved from https://keras.io/examples/cifar10_cnn/

3)https://github.com/gabrielpierobon/cnnshapes/blob/master/README.md
