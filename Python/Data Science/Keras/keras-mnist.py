#Code based on tutorial:
#https://elitedatascience.com/keras-tutorial-deep-learning-in-python

#Great tutorial about convolution in neural networks:
#https://www.youtube.com/watch?v=FmpDIaiMIeA

#Error
#ValueError: Negative dimension size caused by subtracting 3 from 1
#for 'conv2d_1/convolution' (op: 'Conv2D')
#with input shapes: [?,1,28,28], [3,3,28,32]
#Solution
#https://stackoverflow.com/questions/41651628/negative-dimension-size-caused-by-subtracting-3-from-1-for-conv2d

#Run with theano backend (pip3 install theano)
#KERAS_BACKEND=theano python3 keras-mnist.py

import numpy as np

from keras.models import Sequential
from keras.datasets import mnist
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import np_utils

import matplotlib.pyplot as plt

np.random.seed(123)  # for reproducibility

#Print the data of the first image in training set
def print_img_data(num_matrix):

	#Loop all rows
	for row in num_matrix:
		row_str = ""
		#Loop all pixels in the row
		for num in row:
			#Default string, if the number is zero
			num_str = "---"
			#If not zero, print the number
			if num!=0:
				#Zero pad three digits
				num_str = str(num).zfill(3)
			#Append the string of this row
			row_str = row_str + num_str

		#Print this row
		print(row_str)

#Load image data to
(X_train, y_train), (X_test, y_test) = mnist.load_data()

#Show the first image
print("\nShow first image")
plt.imshow(X_train[0])
#plt.show()

#Print data from the first image
#print_img_data(X_train[0])

#Print the first label
print("\nLabel of the first image")
print(y_train[0])

#Print shape before reshape
print("\nShape of training data before re-shape")
print("X")
print(X_train.shape)
print("Y")
print(y_train.shape)

#Re-shape the train and test sets
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)

#Normalize pixels from 0-255 to 0-1
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

# Convert 1-dimensional class arrays to 10-dimensional class matrices
Y_train = np_utils.to_categorical(y_train, 10)
Y_test = np_utils.to_categorical(y_test, 10)

#Print shape after reshape
print("\nShape of training data after re-shape")
print("X")
print(X_train.shape)
print("Y")
print(Y_train.shape)

#Initialize the model
model = Sequential()

#Define the first layer
#32 convolution filters
#Convolution size = 3x3
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28,28,1)))

model.add(Conv2D(32, (3, 3), activation='relu'))

#Print model shape
#Convolution should reduce image dimensions by one pixel from each border
print("\nModel shape:")
print(model.output_shape)

#Max pooling 2x2
model.add(MaxPooling2D(pool_size=(2,2)))
#25% of randomly selected neurons are not activated randomly
model.add(Dropout(0.25))
#Transform the matrix to one dimension for fully connected layer
model.add(Flatten())
#Add the fully connceted layer
model.add(Dense(128, activation='relu'))
#Dropout
model.add(Dropout(0.5))
#The result layer
model.add(Dense(10, activation='softmax'))

#Compile the model
model.compile(
	loss='categorical_crossentropy',
	optimizer='adam',
	metrics=['accuracy']
)

#Fit the model
model.fit(
	X_train,
	Y_train,
	batch_size=32, nb_epoch=10, verbose=1
)

#Test the model
score = model.evaluate(X_test, Y_test, verbose=0)
print(score)

#Getting the result takes 10 x 90 seconds
#[0.025986726288703358, 0.9924]
