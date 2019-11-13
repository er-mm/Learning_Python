# Dictionaries
# A dictionary is a data type similar to arrays, but works with keys and values instead of indexes. 
# Each value stored in a dictionary can be accessed using a key, which is any type of object (a string, a number, a list, etc.) instead of using its index to address it.

# For example, a database of phone numbers could be stored using a dictionary like this:
phonebook = {}
phonebook['Mayank'] = 1234567890
phonebook['Ayush'] = 9876543210
phonebook['Mittal'] = 1357924680
print(phonebook) # {'Mayank': 1234567890, 'Ayush': 9876543210, 'Mittal': 1357924680}

# Alternatively, a dictionary can be initialized with the same values in the following notation:
phonebook2 = {
    'Mayank' : 1234567890,
    'Ayush' : 9876543210,
    'Mittal' : 1357924680
}
print(phonebook2.items()) # dict_items([('Mayank', 1234567890), ('Ayush', 9876543210), ('Mittal', 1357924680)])

# Iterating over dictionaries
# Dictionaries can be iterated over, just like a list. However, a dictionary, unlike a list, does not keep the order of the values stored in it. 
# To iterate over key value pairs, use the following syntax:
for key, value in phonebook.items(): # if using phonebook : ValueError: too many values to unpack (expected 2)
    print("The number of %s is %d." % (key, value))

# Removing a value
# To remove a specified index, use either one of the following notations:
del phonebook['Mayank']
del phonebook2['Ayush']

print(phonebook)
print(phonebook2)

# or:
phonebook.pop('Mittal')
phonebook2.pop('Mittal')

print(phonebook)
print(phonebook2)

# Exercise
# Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
# write your code here
phonebook['Jake'] = 938273443
phonebook.pop('Jill')

# testing code
if 'Jake' in phonebook:
    print('Jake is listed in phonebook')
if 'Jill' not in phonebook:
    print('Jill is not listed in phonebook')