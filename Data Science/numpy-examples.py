import numpy as np

#RANGE
print("\nRange")

#Range of numbers
rng_1 = np.arange(10)
print(rng_1)

#Range of numbers with start and end - 1
rng_2 = np.arange(1,10)
print(rng_2)

#Range of numbers with start, end and step
rng_3 = np.arange(0,11,5)
print(rng_3)


#ARRAY
print("\nArray")
#Create array
dt_1 = np.array([1,2,3])
print(dt_1)

#Show data type
print('Dtype ' + str(dt_1.dtype))

#Change data type
dt_2 = dt_1.astype(np.int64)
print('Dtype ' + str(dt_2.dtype))

