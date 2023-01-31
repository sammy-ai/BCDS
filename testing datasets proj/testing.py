import os 
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_datasets as tfds
#import pandas as pd


#i was importing the datasets and checking their availability
#a=  tfds.list_builders()
#print( a)

#(training_images, training_labels), (testing_images, testing_labels) = datasets.ccurated_breast_imaging_ddsm.load_data()


'''
for i in range(16):     #in this loop we plot few of our dataset on the screen
    plt.subplot(4,4,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(cmap=plt.cm.binary)  # we get the image
    plt.xlabel(class_names[training_labels[i][0]])      #we then print the name of the object under it
    
plt.show()
'''


db = tfds.load('cifar10', split='train')
db = db.take(1)  # Only take a single image as an example

for example in db:  # example is `{'image': tf.Tensor, 'label': tf.Tensor}`
  print(list(example.keys()))
  image = example["image"]
  label = example["label"]
  print(image.shape, label)


#in this loop we plot few of our dataset on the screen
plt.subplot(4,4, db.take(1))
plt.xticks([])
plt.yticks([])
plt.imshow(training_images[db.take(1)],cmap=plt.cm.binary)  # we get the image
#plt.xlabel(class_names[training_labels[i][0]])      #we then print the name of the object under it
    
plt.show() # we then show the data on the screen