# Create class
class Student:
  # Add constructor
  def __init__(self, name, year):
    # Create two instance attributes
    self.name = name
    self.year = year
    # Create empty list self.grades
    self.grades = []

  # Create add_grade() method
  def add_grade(self, grade):
    # If grade is type of Grade
    if (type(grade) == Grade):
      # Append grade to self.grades
      self.grades.append(grade)
  # Create get_average() method
  def get_average(self):
    # Create total_grades
    total_grades = 0
    # Iterate through self.grades
    for grade in self.grades:
      # Add grade to total_grades
      total_grades += grade.score
    # Calculate average of grades
    average_grades = total_grades/len(self.grades)
    # Return average_grades
    return average_grades


# Create 3 Student objects
roger = Student('Roger van der Weyden', 10)
sandro = Student('Sandro Botticelli', 12)
pieter = Student('Pieter Bruegel the Elder', 8)

# Create class
class Grade:
  # Add attribute
  minimum_passing = 65
  # Add constructor
  def __init__(self, score):
    # Create instance attribute
    self.score = score
  # Create is_passsing() method
  def is_passing(self):
    # If self.score > minimum_passing
    if (self.score > self.minimum_passing):
      # Return True
      return True
    # Else self.score < minimum_passing
    else:
      # Return False
      return False

# Create Grade object
pieter.add_grade(Grade(100))
pieter.add_grade(Grade(90))
# Check get_average() method
print(pieter.get_average())
# Check is_passing() method
print(Grade(75).is_passing())
print(Grade(55).is_passing())
