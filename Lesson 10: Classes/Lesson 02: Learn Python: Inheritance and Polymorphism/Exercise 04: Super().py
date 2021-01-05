# super() gives us a proxy object.
# With this proxy object, we can invoke the method of an object’s parent class (also called its superclass). 

class PotatoSalad:
  def __init__(self, potatoes, celery, onions):
    self.potatoes = potatoes
    self.celery = celery
    self.onions = onions

# Create SpecialPotatoSalad subclass from PotatoSalad
class SpecialPotatoSalad(PotatoSalad):
  # Create/override constructor
  def __init__(self, potatoes, celery, onions):
    # Call parent constructor method
    super().__init__(potatoes, celery, onions)
    # Add another variable
    self.raisins = 40
