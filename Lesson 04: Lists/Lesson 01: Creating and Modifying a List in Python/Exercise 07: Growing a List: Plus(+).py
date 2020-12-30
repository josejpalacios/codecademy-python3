# When we want to add multiple items to a list, we can use + to combine two lists.

# We can only use + with other lists.

# If we want to add a single element using +, we have to put it into a list with brackets ([])

orders = ['daisy', 'buttercup', 'snapdragon', 'gardenia', 'lily']

# Create new orders here:
new_orders = orders + ['lilac', 'iris']

# TypeError: an only concatenate list (not "int") to list
# broken_prices = [5, 3, 4, 5, 4] + 4

#Fix TypeError by added [] around 4
broken_prices = [5, 3, 4, 5, 4] + [4]
