# Create list with numbers 0 to 9
single_digits = list(range(10))

# Create empty list squares
squares = []

# Create for loo
for digit in single_digits:
  # Print digit
  print(digit)
  # Append square value of each digit
  squares.append(digit**2)

# Print squares
print(squares)

# Create list cubes using list comprehension
cubes = [digit**3 for digit in single_digits]

# Print cubes
print(cubes)
