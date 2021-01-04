# The data held by an object is referred to as an instance variable.
# Instance variables aren’t shared by all instances of a class
# — they are variables that are specific to the object they are attached to.

class Store:
  pass

# Create Store objects
alternative_rocks = Store()
isabelles_ices = Store()

# Give objects instance attributes
alternative_rocks.store_name = 'Alternative Rocks'
isabelles_ices.store_name = 'Isabelle\'s Ices'
