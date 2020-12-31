# A loop that never terminates is called an infinite loop.
# These are very dangerous for your code!

# A program that hits an infinite loop often becomes completely unusable.
# The best course of action is to never write an infinite loop.

students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

# Create for loop
for student in students_period_A:
  # Switching B to A causes an infinite loop
  students_period_B.append(student)
  print(student)
