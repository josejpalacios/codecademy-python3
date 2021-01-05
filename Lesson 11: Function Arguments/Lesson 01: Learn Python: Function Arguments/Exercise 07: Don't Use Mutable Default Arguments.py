# A mutable object refers to various data structures in Python that are intended to be mutated, or changed.

# A list has append and remove operations that change the nature of a list.
# Sets and dictionaries are two other mutable objects in Python.

# It might be helpful to note some of the objects in Python that are not mutable
# (and therefore OK to use as default arguments).

# int, float, and other numbers can’t be mutated (arithmetic operations will return a new number).
# tuples are a kind of immutable list. Strings are also immutable — operations that update a string will all return a completely new string.

def update_order(new_item, current_order=[]):
  current_order.append(new_item)
  return current_order

# First order, burger and a soda
order1 = update_order({'item': 'burger', 'cost': '3.50'})
order1 = update_order({'item': 'soda', 'cost': '1.50'}, order1)

# Second order, just a soda
order2 = update_order({'item': 'soda', 'cost': '1.50'})

# What's in that second order again?
print(order2)

# Fix in the next exercise
