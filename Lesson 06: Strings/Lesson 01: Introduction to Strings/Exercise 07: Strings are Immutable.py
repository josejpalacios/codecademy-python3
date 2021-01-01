# This is because strings are immutable.
# This means that we cannot change a string once it is created.
# We can use it to create other strings, but we cannot change the string itself.

# This property, generally, is known as mutability.
# Data types that are mutable can be changed,
# and data types, like strings, that are immutable cannot be changed.

first_name = "Bob"
last_name = "Daily"

# TypeError: 'str' object does not support item assignment
# first_name[0] = "R"

# Create new string
fixed_first_name = "R" + first_name[1:]
print(fixed_first_name)
