# Conditions
# Python uses boolean variables to evaluate conditions. The boolean values True and False are returned when an expression is compared or evaluated. For example:
number = 2
print(number == 2) #True
print(number == 3) #False
print(number > 2) #False
print(number >= 2) #True

# Boolean operators
# The "and" and "or" boolean operators allow building complex boolean expressions, for example:
name = "Mayank"
age = 24
if name == "Mayank" and age == 24:
    print("Your name is %s and also your age is %d." %(name, age))
if name == "Mayank" or name == "MM":
    print("Your name is either %s or MM." % name)

# The "in" operator
# The "in" operator could be used to check if a specified object exists within an iterable object container, such as a list:
listOfNames = ["Aakash", "Ankur", "Kapil", "Mayank"]
nameToFind = "Mayank"
if nameToFind in listOfNames:
    print("Name found")

# Python uses indentation to define code blocks, instead of brackets. The standard Python indentation is 4 spaces, although tabs and any other space size will work, as long as it is consistent. Notice that code blocks do not need any termination.
# Here is an example for using Python's "if" statement using code blocks:
x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

# Here are some examples for objects which are considered as empty: 1. An empty string: "" 2. An empty list: [] 3. The number zero: 0 4. The false boolean variable: False

# The 'is' operator
# Unlike the double equals operator "==", the "is" operator does not match the values of the variables, but the instances themselves. For example:
list1 = [1,2,3]
list2 = [1,2,3]
print(list1 == list2)
print(list1 is list2)

# The "not" operator
# Using "not" before a boolean expression inverts it:
print(not False)
print(not False != False)
print(not (2 == 3))

# Exercise
# Change the variables in the first section, so that each if statement resolves as True.
# ================Question===================
# change this code
number = 10
second_number = 10
first_array = []
second_array = [1,2,3]

# ============ChangedCode============
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")