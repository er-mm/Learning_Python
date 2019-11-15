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
print(numpy_height)

# Element-wise calculations
# Now we can perform element-wise calculations on height and weight. 
# For example, you could take all 6 of the height and weight observations above, and calculate the BMI for each observation with a single equation. 
# These operations are very fast and computationally efficient. 
# They are particularly helpful when you have 1000s of observations in your data.

# Calculate BMI
bmi = (numpy_height + numpy_weight) ** 2
print(bmi)

# Subsetting
# Another great feature of Numpy arrays is the ability to subset. 
# For instance, if you wanted to know which observations in our BMI array are above 4500, we could quickly subset it to find out.
print(bmi[bmi > 4500])

# Exercise
# First, convert the list of weights from a list to a Numpy array. 
# Then, convert all of the weights from kilograms to pounds. Use the scalar conversion of 2.2 lbs per kilogram to make your conversion. 
# Lastly, print the resulting array of weights in pounds.

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Create a numpy array np_weight_kg from weight_kg
np_weight_kg = np.array(weight_kg)

# Create np_weight_lbs from np_weight_kg
np_weight_lbs = np_weight_kg * 2.2

# Print out np_weight_lbs
print(np_weight_lbs)