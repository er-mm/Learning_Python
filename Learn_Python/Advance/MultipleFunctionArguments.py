# Multiple Function Arguments
# Every function in Python receives a predefined number of arguments, if declared normally
# It is possible to declare functions which receive a variable number of arguments, using the following syntax:
# The "rest" variable is a list of variables, which receives all arguments which were given to the "foo"
# function after the first 3 arguments. So calling foo(1,2,3,4,5) will print out:

def foo(first, second, third, *rest):
    print(first)
    print(second)
    print(third)
    print(rest)
    print(list(rest))


foo(1, 2, 3, 4, 5)


# It is also possible to send functions arguments by keyword, so that the order of the argument does not matter,
# using the following syntax. The following code yields the following output: The sum is: 6 Result: 1
def bar(first, second, third, **action):
    print(first)
    print(second)
    print(third)
    print(action)
    print(action.get('add'))
    print(action.get('number'))
    if action.get('add') == 'sum':
        print('sum is = %d.' % (first + second + third))
    if action.get('number') == "first":
        return first


result = bar(1, 2, 3, add="sum", number="first")
print('result is = %d.' % result)

# Exercise
# Fill in the foo and bar functions so they can receive a variable amount of arguments (3 or more)
# The foo function must return the amount of extra arguments received.
# The bar must return True if the argument with the keyword magicnumber is worth 7, and False otherwise.

# edit the functions prototype and implementation
# def foo(a, b, c):
#     pass
#
# def bar(a, b, c):
#     pass
print("=======Exercise======")


def foo1(a, b, c, *extraArgs):
    return len(extraArgs)


def bar1(a, b, c, **action):
    return action['magicnumber'] == 7  # action.get('magicnumber) OR action['magicnumber']


# test code
if foo1(1, 2, 3, 4) == 1:
    print("Good.")
if foo1(1, 2, 3, 4, 5) == 2:
    print("Better.")
if not bar1(1, 2, 3, magicnumber=6):
    print("Great.")
if bar1(1, 2, 3, magicnumber=7):
    print("Awesome!")
