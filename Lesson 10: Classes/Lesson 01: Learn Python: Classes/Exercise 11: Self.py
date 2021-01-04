class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = diameter/2
  # Create new circumference
  def circumference(self):
    # Return circumference of a circle
    return 2 * self.pi * self.radius

# Create 3 Circle objects
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

# Print circumferences of 3 Cirle objects
print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())
