# One way that we can introduce polymorphism to our class definitions
# is by using Python’s special dunder methods.

# __init__() the constructor for a class
# __repr__ the string representation method
# __add__ the use of + symbol to add perform addition

# Python gives us the power to define dunder methods that define a 
# custom-made class to look and behave like a Python builtin. 

class Atom:
  def __init__(self, label):
    self.label = label
  # Create __add__ dunder method
  def __add__(self, other):
    # Create list of Atom objects
    atoms = [self, other]
    # Return Molecule with atoms as input
    return Molecule(atoms)
    
class Molecule:
  def __init__(self, atoms):
    if type(atoms) is list:
	    self.atoms = atoms
      
sodium = Atom("Na")
chlorine = Atom("Cl")
salt = Molecule([sodium, chlorine])
salt = sodium + chlorine
