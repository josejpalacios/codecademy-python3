# There are several methods that we can define in a Python class that have special behavior.
# These methods are sometimes called “magic,” because they behave differently from regular methods.
# Another popular term is dunder methods, so-named because they have two underscores (double-underscore abbreviated to “dunder”) on either side of them.

# The first dunder method we’re going to use is the __init__() method
# (note the two underscores before and after the word “init”).

# This method is used to initialize a newly created object.
# It is called every time the class is instantiated.

# Methods that are used to prepare an object being instantiated are called constructors.
# The word “constructor” is used to describe similar features in other object-oriented programming languages
# but programmers who refer to a constructor in Python are usually talking about the __init__() method.

# Parameters can be received by the __init__() method.
class Circle:
  pi = 3.14
  
  # Add constructor here:
  def __init__(self, diameter):
    # Print message
    print('New circle with diameter: {diameter}'.format(diameter=diameter))

# Create Circle instance
teaching_table = Circle(36)
