# Write a function named frequency_dictionary that takes a list of elements named words as a parameter.
# The function should return a dictionary containing the frequency of each element in words.

# Write your frequency_dictionary function here:
def frequency_dictionary(words):
  # Create empty dictionary
  frequency = {}
  # Iterate through words
  for word in words:
    # Add key value pair of word and its appearances in words
    frequency[word] = words.count(word)
  # Return frequency
  return frequency
  
# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}
