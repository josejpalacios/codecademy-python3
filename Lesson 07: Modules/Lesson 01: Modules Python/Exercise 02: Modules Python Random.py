# random allows you to generate numbers or select items at random.

# random.choice() which takes a list as an argument and returns a number from the list
# random.randint() which takes two numbers as arguments and generates a random number between the two numbers you passed in

# Import random below:
import random

# Create random_list below:
random_list = []
# Use list comprehension
random_list = [random.randint(1, 100) for num in range(101)]

# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)
