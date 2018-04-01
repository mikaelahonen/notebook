from keras.datasets import mnist

(X_train, y_train), (X_test, y_test) = mnist.load_data()

#Print the label
print(y_train[0])

#Print the data
num_matrix = X_train[0]
for row in num_matrix:
	row_str = ""
	for num in row:
		row_str = row_str + "," + str(num)
	print(row_str)