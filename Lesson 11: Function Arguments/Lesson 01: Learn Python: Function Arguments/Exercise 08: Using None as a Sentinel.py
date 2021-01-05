# We can use None as a special value to indicate we did not receive anything.

# Change default value of empty list to None
def update_order(new_item, current_order=None):
  # If current_order is None
  if (current_order is None):
    # Set current_order to an empty list
    current_order = []

  current_order.append(new_item)
  return current_order

# First order, burger and a soda
order1 = update_order({'item': 'burger', 'cost': '3.50'})
order1 = update_order({'item': 'soda', 'cost': '1.50'}, order1)

# Second order, just a soda
order2 = update_order({'item': 'soda', 'cost': '1.50'})

# What's in that second order again?
print(order2)
