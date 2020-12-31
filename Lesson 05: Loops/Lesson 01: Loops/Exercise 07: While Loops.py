# The while loop performs a set of code until some condition is reached.

# While loops can be used to iterate through lists, just like for loops

# While loops can be useful when you don’t know how many iterations it will take to satisfy a condition.

all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

# Create while loop
while (len(students_in_poetry) < 6):
  # Remove student from all_students
  student = all_students.pop()
  # Add student to students_in_poetry
  students_in_poetry.append(student)

print(students_in_poetry)
