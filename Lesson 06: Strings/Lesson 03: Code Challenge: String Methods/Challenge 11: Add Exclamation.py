# Create a function named add_exclamation that has one parameter named word.
# This function should add exclamation points to the end of word until word is 20 characters long.
# If word is already at least 20 characters long, just return word.

# Write your add_exclamation function here:
def add_exclamation(word):
  # While length of word < 20
  while(len(word) < 20):
    # Add exclamation point
    word += "!"
  # Return word
  return word

# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn