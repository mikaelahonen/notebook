# Numpy
Numpy is a python library for multidimensional arrays.

Dimensions are called axes.

Numpy's array class name is `ndarray` (n dimensional array) 
which can be referred as `numpy.array`. It is different
from python's native `array.array`.

Array properties:
* `ndarray.ndim` Number of axes (dimensions) in array.
* `ndarray.shape` Size of each axes.
* `ndarray.size` Total number of elements. 
* `ndarray.dtype` Array data type. All of the elements should be same type. NumPy also offers its own data types. 
* `ndarray.itemsize` Byte size of array elements.
* `ndarray.data` Cache for all array elements. 

NumPy methods for arrays:
* Create random numbers
* Create sequences
* Change data types
* Shape, slice, stack
* Take matrix product
* sum, sin, cos, exp, sqrt

[NumPy docs](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html)

NumPy can be imported for example like this `import numpy as np`.
After which you can refer to it like:

`x = np.array([1,2,3])`