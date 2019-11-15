# Pandas
# Pandas DataFrames
# Pandas is a high-level data manipulation tool developed by Wes McKinney.
# It is built on the Numpy package and its key data structure is called the DataFrame.
# DataFrames allow you to store and manipulate tabular data in rows of observations and columns of variables.
# There are several ways to create a DataFrame. One way way is to use a dictionary. For example:


organizationalData = {
    'empName': ['Mayank', 'Akash', 'Ankur', 'Kapil', 'Sudhanshu'],
    'department': ['Development', 'DataScience', 'Development', 'Sales', 'Testing'],
    'location': ['Noida', 'Gurugram', 'Noida', 'Noida', 'Pune'],
    'organization': ['GlobalLogic', 'Dunhumby', 'TechMahindra', 'AppiPie', 'Wipro']
}

import pandas as pd

organizationalDataAsDataFrame = pd.DataFrame(organizationalData)
# print(organizationalDataAsDataFrame)
print('-------------------------------------------------------')

# As you can see with the new organizationalDataAsDataFrame DataFrame, Pandas has assigned a key for each empName as the numerical values 0 through 4.
# If you would like to have different index values, say, the shortform of department names, you can do that easily as well.
organizationalDataAsDataFrame.index = ['Dev', 'DS', 'Dev', 'S', 'Test']
# print(organizationalDataAsDataFrame)
print('-------------------------------------------------------')

# Another way to create a DataFrame is by importing a csv file using Pandas.
# Now, the csv organizationalDataAsDataFrame.csv is stored and can be imported using pd.read_csv:
organizationalDataAsDataFrame = pd.read_csv('../organizationalDataAsDataFrame.csv', index_col = 0)
print(organizationalDataAsDataFrame)

# Indexing DataFrames
# There are several ways to index a Pandas DataFrame.
# One of the easiest ways to do this is by using square bracket notation.
# you can use square brackets to select 1 or more columns of the DataFrame
# print(organizationalDataAsDataFrame["empName"])
print('-------------------------------------------------------')
# You can either use a single bracket or a double bracket.
# The single bracket with output a Pandas Series, while a double bracket will output a Pandas DataFrame.
# print(organizationalDataAsDataFrame[["empName"]])
print('-------------------------------------------------------')
# print(organizationalDataAsDataFrame[["empName", "department"]])

# Square brackets can also be used to access observations (rows) from a DataFrame. For example:
# print(organizationalDataAsDataFrame[0:2]) # print first two observations
# print(organizationalDataAsDataFrame[2:5]) # print print 3,4 and 5th observation

# You can also use loc and iloc to perform just about any data selection operation.
# loc is label-based, which means that you have to specify rows and columns based on their row and column labels.
# iloc is integer index based, so you have to specify rows and columns by their integer index like you did in the previous exercise.
print(organizationalDataAsDataFrame.loc[['S', 'DS']])
print('-------------------------------------------------------')
print(organizationalDataAsDataFrame.iloc[2, 3])
