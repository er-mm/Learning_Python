# Classes and Objects
# Objects are an encapsulation of variables and functions into a single entity. Objects get their variables and functions from classes. Classes are essentially a template to create your objects.
# A very basic class would look something like this:
class LearnPython:
    name = "Python"
    def pythonFunction(self):
        print("This is pythonFunction inside LearnPython Class")

# First, to assign the above class(template) to an object you would do the following:
classObj = LearnPython()

# Now the variable "classObj" holds an object of the class "LearnPython" that contains the variable and the function defined within the class called "LearnPython".

# Accessing Object Variables
# To access the variable inside of the newly created object "classObj" you would do the following:
print(classObj.name)
# So for instance the below would output the string "Python":

# You can create multiple different objects that are of the same class(have the same variables and functions defined). However, each object contains independent copies of the variables defined in the class. For instance, if we were to define another object with the "LearnPython" class and then change the string in the variable above:
classObj2 = LearnPython()
classObj2.name = "Learn"
print(classObj.name)
print(classObj2.name)

# Accessing Object Functions
# To access a function inside of an object you use notation similar to accessing a variable:
classObj.pythonFunction()
# The above would print out the message, "This is pythonFunction inside LearnPython Class"

# Exercise
# We have a class defined for vehicles. Create two new vehicles called car1 and car2. 
# Set car1 to be a red convertible worth $60,000.00 with a name of Fer, and car2 to be a blue van named Jump worth $10,000.00.
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = "0.00"
    def description(self):
        car_desc = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return car_desc

car1 = Vehicle()
car1.name = "convertible"
car1.color = "red"
car1.value = 60000

car2 = Vehicle()
car2.name = "van"
car2.color = "blue"
car2.value = 10000

print(car1.description())
print(car2.description())


