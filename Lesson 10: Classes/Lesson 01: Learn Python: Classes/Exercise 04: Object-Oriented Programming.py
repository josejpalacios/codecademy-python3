# A class instance is also called an object.
# The pattern of defining classes and creating objects to represent the
# responsibilities of a program is known as Object Oriented Programming or OOP.

# Instantiation takes a class and turns it into an object,
# the type() function does the opposite of that.
# When called with an object, it returns the class that the object is an instance of.

# In Python __main__ means “this current file that we’re running”

class Facade:
  pass

facade_1 = Facade()
# Call type() on facade_1
facade_1_type = type(facade_1)
# Print facade_1_type
print(facade_1_type)
