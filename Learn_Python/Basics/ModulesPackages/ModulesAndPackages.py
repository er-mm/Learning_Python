# Modules and Packages
# In programming, a module is a piece of software that has a specific functionality. 
# For example, when building a ping pong game, one module would be responsible for the game logic, and
# another module would be responsible for drawing the game on the screen. Each module is a different file, which can be edited separately.

# Writing modules
# Modules in Python are simply Python files with a .py extension. 
# The name of the module will be the name of the file. A Python module can have a set of functions, classes or variables defined and implemented. 


import Calc # or from Calc import * # We may also use the import * command to import all objects from a specific module
# Import a particular function ( from Calc import sum)
import urllib #python library 

sum = Calc.add(1,2)
sub = Calc.sub(1,2)
mul = Calc.mul(1,2)
div = Calc.div(1,2)

sortedList = Calc.sortList([22,11,14,15,6,3])
print(sortedList)

sortedList = Calc.sortList(['ab','aa','da','aca'])
print(sortedList)

def main():
    initialize = (sum,sub,mul,div)
    result = "sum is = %d, sub is = %d, mul is = %d, div is = %.1f." % initialize
    print(result)

if __name__ == '__main__':
    main()

# Module initialization
# The first time a module is loaded into a running Python script, it is initialized by executing the code in the module once. 
# If another module in your code imports the same module again, it will not be loaded twice but once only - so local variables inside the module act as a "singleton" - they are initialized only once.


