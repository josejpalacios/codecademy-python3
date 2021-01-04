# We can use the dir() function to investigate an object’s attributes at runtime.
# dir() is short for directory and offers an organized presentation of object attributes.

# Call dir() on 5 and print results
print(dir(5))

# Create function
def this_function_is_an_object(num):
  # Return num * 2
  return num * 2

# Call dir on this_function_is_an_object and print results
print(dir(this_function_is_an_object))
