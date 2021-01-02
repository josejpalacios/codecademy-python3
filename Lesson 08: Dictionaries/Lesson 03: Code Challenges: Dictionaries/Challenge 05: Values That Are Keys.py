# Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter.
# This function should return a list of all values in the dictionary that are also keys.

# Write your values_that_are_keys function here:
def values_that_are_keys(my_dictionary):
  # Create empty list
  value_key_list = []
  # Iterate through values of my_dictionary
  for value in my_dictionary.values():
    # If value is a key
    if (value in my_dictionary):
      # Append value to value_key_list
      value_key_list.append(value)
  # Return value_key_list
  return value_key_list

# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]
