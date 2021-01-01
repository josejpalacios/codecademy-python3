# Python comes with some built-in functions for working with strings.
# One of the most commonly used of these functions is len().
# len() returns the number of characters in a string

# The last character in a string has an index that is len(string_name) - 1.

# Using a len() statement as the starting index and omitting the final index
# lets you slice n characters from the end of a string, where n is the amount
# you subtract from len().

first_name = "Reiko"
last_name = "Matsuki"

# Write password_generator function
def password_generator(first_name, last_name):
  # Get length of names
  first_length = len(first_name)
  last_length = len(last_name)
  # Get last three letters of both names
  first = first_name[first_length-3:]
  last = last_name[last_length-3:]
  # Concatenate strings
  new_password = first + last
  # Return string
  return new_password

# Test function
temp_password = password_generator(first_name, last_name)
