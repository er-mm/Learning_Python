# String Formatting
#Python uses C-style string formatting to create new, formatted strings. The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s" and "%d".

# This prints out "Hello, Mayank!"
name = "Mayank"
print("Hello, %s!" % name)

# To use two or more argument specifiers, use a tuple (parentheses):
name = "Mayank"
age = 24
print("%s is %d years old." % (name, age))

# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s" % mylist)

#Here are some basic argument specifiers you should know:
# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)

#Exercise : You will need to write a format string which prints out the data using the following syntax: Hello John Doe. Your current balance is $53.44.
firstName = "Mayank"
lastName = "Mittal"
balance = 53.44
data = (firstName, lastName, balance)
print("Hello %s %s. Your current bal is $%.2f." % data)

format_string = "Hello %s %s. Your current balance is $%.2f."
print(format_string % data)

