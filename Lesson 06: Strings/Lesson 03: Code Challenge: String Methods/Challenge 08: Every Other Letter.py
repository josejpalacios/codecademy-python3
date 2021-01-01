# Create a function named every_other_letter that takes a string named word as a parameter.
# The function should return a string containing every other letter in word.

# Write your every_other_letter function here:
def every_other_letter(word):
  # Create variable substring
  substring = ""
  # Iterate through word indices skipping by 2
  for index in range(0, len(word), 2):
    # Add value at index to substring
    substring += word[index]
  # Return substring
  return substring

# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 
