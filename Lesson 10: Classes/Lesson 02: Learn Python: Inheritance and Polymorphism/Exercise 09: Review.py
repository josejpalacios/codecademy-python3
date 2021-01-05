# Create subclass
class SortedList(list):
  # Create __init__() dunder method
  def __init__(self, values):
    # Call __init__ of super
    super().__init__(values)
    # Sort list using super()
    super().sort()

  # Overwrite append method
  def append(self, value):
    # Add value to list using super()
    super().append(value)
    # Sort list using super()
    super().sort()

sorted_list = SortedList([4, 1, 5])
print(sorted_list)
sorted_list.append(3)
print(sorted_list)
