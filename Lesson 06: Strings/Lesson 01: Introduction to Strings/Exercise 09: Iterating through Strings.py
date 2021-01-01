# Because strings are lists, that means we can iterate through a string using for or while loops.

# Write get_length function
# Works like len()
def get_length(word):
  # Variable to count
  count = 0
  # Iterate through string
  for letter in word:
    # Increment count by 1
    count += 1
  # Return count
  return count
