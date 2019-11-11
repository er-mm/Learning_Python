# Arithmetic Operators
#Just as any other programming languages, the addition, subtraction, multiplication, and division operators can be used with numbers.

addMullSubDiv = ((4 + 3) * 2) / float(7)
print("Calculated result = %f " % addMullSubDiv)

# Another operator available is the modulo (%) operator, which returns the integer remainder of the division. dividend % divisor = remainder.

remainder = 11 % 3
print("Remainder is: %d " %remainder)

# Using two multiplication symbols makes a power relationship.

square = 3 ** 2
print("Square of 3 is: %d " % square)
cube = 3 ** 3
print("Cube of 3  is: %d " % cube)

# Using Operators with Strings
# Python supports concatenating strings using the addition operator:

concatinatedString = "Hello" + " " + "world " + "!!"
print("concatinatedString is: %s " % concatinatedString)

# Python also supports multiplying strings to form a string with a repeating sequence:

multiplyString = "Hello " * 3
print("multiply hello 3 times: %s " % multiplyString)

# Using Operators with Lists
# Lists can be joined with the addition operators:

oddList = [1,3,5]
evenList = ['2',4,6]
joinList = oddList + evenList
print(joinList)

# Just as in strings, Python supports forming new lists with a repeating sequence using the multiplication operator:

multiplyList = [1,2] * 3
print(multiplyList)

# Exercise : The target of this exercise is to create two lists called x_list and y_list, which contain 10 instances of the variables x and y, respectively. You are also required to create a list called big_list, which contains the variables x and y, 10 times each, by concatenating the two lists you have created.

x = 'x'
y = 'y'
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list
print('x_list contains %d x ' % len(x_list))
print('y_list contains %d y ' % len(y_list))
print('big_list contains %d x and y ' % len(big_list))

#testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print('x and y are both 10')
if big_list.count(x) == 10 and big_list.count(y) == 10 and len(big_list) == 20:
    print('big list has both 10 10 x and y with count 20')
