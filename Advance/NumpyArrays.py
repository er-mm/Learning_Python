# Numpy Arrays
# Numpy arrays are great alternatives to Python Lists. 
# Some of the key advantages of Numpy arrays are that they are fast, easy to work with, and give users the opportunity to perform calculations across entire arrays.
# In the following example, you will first create two Python lists. Then, you will import the numpy package and create numpy arrays out of the newly created lists.

# Create two list of height and weight
height = [4.2, 5.4, 5.8, 6.2, 7.1]
weight = [49.5, 60.4, 68.2, 70.4, 80.5]

# import the numpy package as np
import numpy as np

# create two numpy arrays from the above lists
numpy_height = np.array(height)
numpy_weight = np.array(weight)

# Print out the type of np_height
print(type(numpy_height))
