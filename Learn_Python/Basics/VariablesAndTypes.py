# Python is completely object oriented, and not "statically typed". You do not need to declare variables before using them, or declare their type. Every variable in Python is an object.

# NUMBERS (Python supports two types of numbers - integers and floating point numbers. (It also supports complex numbers))
# To define an integer, use the following syntax:

intNumber = 7
print("intNumber %d " % intNumber)

# To define a floating point number, you may use one of the following notations:

floatNumber1 = 7.0
print("floatNumber1 %f " % floatNumber1)
floatNumber2 = float(7)
print("floatNumber2 %f " % floatNumber2)

# STRINGS (Strings are defined either with a single quote or a double quotes.)

stringWithSingleQuotes = 'string With SingleQuotes'
print(stringWithSingleQuotes)
stringWithDoubleQuotes = "string WithDouble Quotes"
print(stringWithDoubleQuotes)

# The difference between the two is that using double quotes makes it easy to include apostrophes (whereas these would terminate the string if using single quotes)

stringWithApostrophes = "it's also working with apostrophes"
print(stringWithApostrophes)

# Simple operators can be executed on numbers and strings:
one = 1
two = 2
three = one + two
print("Sum is %d " % three)

string1 = "Hello"
string2 = "World"
concatString = string1 + " " + string2
print(concatString)

# Assignments can be done on more than one variable "simultaneously" on the same line like this

num1, num2 = 1, 2
print(num1, num2)

# Mixing operators between numbers and strings is not supported:

num1 = 1
num2 = 2
string1 = "string"
# print(num1 + num2 + string1)

# Exercise : The target of this exercise is to create a string, an integer, and a floating point number. The string should be named mystring and should contain the word "hello". The floating point number should be named myfloat and should contain the number 10.0, and the integer should be named myint and should contain the number 20.

# change this code
mystring = "hello"
myfloat = float(10)
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)