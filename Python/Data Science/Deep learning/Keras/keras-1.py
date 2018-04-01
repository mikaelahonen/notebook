from keras.models import Sequential
from keras.layers.core import Dense

#A sequential Keras model is a linear pipeline (a stack) of neural networks layers. 
model = Sequential()

#A single layer with 12 artificial neurons, and it expects 8 input variables
d = Dense(12, input_dim=8, kernel_initializer='random_uniform')

model.add(d)