# Write letter_check function
def letter_check(word, letter):
  # Iterate through word
  for char in word:
    # If char equals letter
    if (char == letter):
      # Return True
      return True
  # Return False
  return False
