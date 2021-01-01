# in checks if one string is part of another string.
# Using in results in a boolean expression

# Write contains function
def contains(big_string, little_string):
  # If little_string in big_string
  if(little_string in big_string):
    # Return True
    return True
  # Return False
  return False

# Write common_letters
def common_letters(string_one, string_two):
  # Create empty list
  common = []
  # Iterate through string one
  for letter in string_one:
    # If letter in string_two and not in common
    if((letter in string_two) and (letter not in common)):
      # Append letter to common
      common.append(letter)
  # Return common
  return common
