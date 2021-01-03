# Create class
class Circle:
  # Create class variable
  pi = 3.14
  # Create method
  def area(self, radius):
    # Return area of circle
    return self.pi * radius ** 2

# Create instance of Circle
circle = Circle()
# Call area method 3 times
pizza_area = circle.area(12/2)
teaching_table_area = circle.area(36/2)
round_room_area = circle.area(11460/2)
