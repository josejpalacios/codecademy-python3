# Write a function named sum_values that takes a dictionary named my_dictionary as a parameter.
# The function should return the sum of the values of the dictionary

# Write your sum_values function here:
def sum_values(my_dictionary):
  # Create total_values
  total_values = 0
  # Iterate through values of dictionary
  for value in my_dictionary.values():
    # Add value to total_values
    total_values += value
  # Return total_values
  return total_values

# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6
