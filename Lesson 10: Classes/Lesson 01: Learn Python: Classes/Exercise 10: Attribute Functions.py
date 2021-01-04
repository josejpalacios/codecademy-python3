# Instance variables and class variables are both attributes of an object

# hasattr() Python function that will return True if an object has a given attribute and False otherwise.

# getattr() Python function that will return the value of a given object and attribute.
# In this function, we can also supply a third argument that will be
# the default if the object does not have the given attribute.

# hasattr(object, “attribute”) has two parameters:
# - object : the object we are testing to see if it has a certain attribute
# - attribute : name of attribute we want to see if it exists

# getattr(object, “attribute”, default) has three parameters (one of which is optional):
# - object : the object whose attribute we want to evaluate
# - attribute : name of attribute we want to evaluate
# - default : the value that is returned if the attribute does not exist (note: this parameter is optional)

# Dictionaries and integers both do not have a count attribute, while strings and lists do.

can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]
# Iterate through list
for element in can_we_count_it:
  # If item has attribute count
  if(hasattr(element, 'count')):
    # Print message
    print(str(type(element)) + " has the count attribute!")
  # Else item does not have attribute count
  else:
    # Print message
    print(str(type(element)) + " does not have the count attribute :(")
