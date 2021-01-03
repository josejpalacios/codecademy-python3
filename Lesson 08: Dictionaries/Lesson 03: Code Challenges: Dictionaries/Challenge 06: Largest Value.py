# Write a function named max_key that takes a dictionary named my_dictionary as a parameter.
# The function should return the key associated with the largest value in the dictionary.

# Write your max_key function here:
def max_key(my_dictionary):
  # Store a key from my_dictionary as largest_value
  largest_key = list(my_dictionary.keys())[0]
  # Iterate through keys of my_dictionary
  for key in my_dictionary.keys():
    # If largest_key value < key value
    if (my_dictionary[largest_key] < my_dictionary[key]):
      # Set largest_key equal to key
      largest_key = key
  # Return largest_key
  return largest_key

# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"
