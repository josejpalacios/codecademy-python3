# Write a function named reverse_string that has a string named word as a parameter.
# The function should return word in reverse.

# Write your reverse_string function here:
def reverse_string(word):
  # Create reverse variable
  reverse = ""
  # Iterate through word indices
  for index in range(len(word)-1, -1, -1):
    # Add letter to reverse
    reverse += word[index]
  # Return reverse
  return reverse
# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print
