#https://elitedatascience.com/keras-tutorial-deep-learning-in-python
#Next continue from step 5

#Run with theano backend (pip3 install theano)
#KERAS_BACKEND=theano python3 keras-mnist.py

import numpy as np

from keras.models import Sequential
from keras.datasets import mnist
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils

import matplotlib.pyplot as plt

np.random.seed(123)  # for reproducibility

#Load image data to
(X_train, y_train), (X_test, y_test) = mnist.load_data()

print("\nImage training data shape")
print(X_train.shape)

print("\nShow first image")
plt.imshow(X_train[0])
plt.show()

#Print the first label
print("\nLabel of the first image")
print(y_train[0])

#Print the data
def print_img_data(X_train):
	num_matrix = X_train[0]
	for row in num_matrix:
		row_str = ""
		for num in row:
			row_str = row_str + "," + str(num)
		print(row_str)
