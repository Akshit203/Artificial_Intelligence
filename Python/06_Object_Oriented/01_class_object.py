#######################################################################################

# Without using a constructor (__init__)

class Car1:
    # Class-level attributes (shared among all instances unless overridden)
    model = None
    brand = None

# Object creation
new_car1 = Car1()

# Manually assigning value to brand after object creation
new_car1.brand = "Mercedes Benz"

print(new_car1.brand)  # Output: Mercedes Benz


#######################################################################################

# Using a constructor (__init__)

class Car2:
    # Constructor method
    def __init__(self, brand, model):
        # Instance variables (unique to each object)
        self.brand = brand
        self.model = model

# Object creation with required values
new_car2 = Car2("Maruti Suzuki", "Alto LXI")

print(new_car2.brand)  # Output: Maruti Suzuki
print(new_car2.model)  # Output: Alto LXI

# Notes:
# __init__ is a special method called a constructor.
# It is automatically invoked when an object is created.
# It ensures that each object is initialized with its own values.
# It makes the code cleaner and reduces chances of missing attributes.


#######################################################################################

# Defining a class with no constructor or attributes

class Test:
    pass  # Placeholder to define an empty class

# Object creation
new_car3 = Test()

# Adding attribute manually after object creation
new_car3.brand = "Hyundai"

print(new_car3.brand)  # Output: Hyundai


#######################################################################################

# Invalid class structure without assignment

'''
class Car:
    model
    brand

new_car = Car()
new_car.model = "AK"
print(new_car.model)  

# This will cause a SyntaxError or NameError in Python.

# Why?
# In Python, you cannot declare variables like this without assigning a value.
# You must assign a value (e.g., model = None) to define class-level attributes.
'''


#######################################################################################
