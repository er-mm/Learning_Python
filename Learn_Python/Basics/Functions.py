# Functions
# Functions are a convenient way to divide your code into useful blocks, allowing us to order our code, make it more readable, reuse it and save some time. Also functions are a key way to define interfaces so programmers can share their code.
# How do you write functions in Python?
# As we have seen on previous tutorials, Python makes use of blocks.
# A block is a area of code of written in the format of:

#block_head:
#    1st block line
#    2nd block line
#    ...

# Where a block line is more Python code (even another block), and the block head is of the following format: block_keyword block_name(argument1,argument2, ...) Block keywords you already know are "if", "for", and "while".
# Functions in python are defined using the block keyword "def", followed with the function's name as the block's name. For example:
def my_func():
    print("Hello From my func")
my_func()

# Functions may also receive arguments (variables passed from the caller to the function). For example:
fName, lName = "Mayank", "Mittal"
def my_fullName(first, last):
    print("My Full name is %s %s." % (first, last))
my_fullName(fName,lName)

# Functions may return a value to the caller, using the keyword- 'return' . For example:
a, b = 10, 20
def sum(first,second):
    return first + second
sumNumber = sum(a,b)
print("sum of a and b is %d." % sumNumber)
### or ###
print("sum of a and b is %d." % sum(a,40))

# How do you call functions in Python?
# Simply write the function's name followed by (), placing any required arguments within the brackets. For example, lets call the functions written above (in the previous example):

# Exercise
# In this exercise you'll use an existing function, and while adding your own to create a fully functional program.
# Add a function named list_benefits() that returns the following list of strings: "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"
# Add a function named build_sentence(info) which receives a single argument containing a string and returns a sentence starting with the given string and ending with the string " is a benefit of functions!"
# Run and see all the functions work together!

# Modify this function to return a list of strings as defined above
def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()