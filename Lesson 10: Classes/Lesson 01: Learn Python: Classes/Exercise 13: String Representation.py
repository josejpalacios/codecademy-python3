# __repr__() is a method we can use to tell Python what we want the string representation of the class to be.
# __repr__() can only have one parameter, self, and must return a string.

class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius

  # Add __repr__() method
  def __repr__(self):
    # Return string
    return 'Circle with radius {radius}'.format(radius=self.radius)
  
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

# Print Circle objects
print(medium_pizza)
print(teaching_table)
print(round_room)
