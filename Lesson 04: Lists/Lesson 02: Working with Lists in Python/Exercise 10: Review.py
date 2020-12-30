inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']

# Get length of inventory
inventory_len = len(inventory)

# Get first element of inventory
first = inventory[0]

# Get last element of inventory
last = inventory[-1]

# Slice from 2 up to but not including 6
inventory_2_6 = inventory[2:6]

# Get first 3 elements
first_3 = inventory[:3]

# Count twin beds
twin_beds = inventory.count('twin bed')

# Sort using .sort()
inventory.sort()

# Print inventory sorted
print(inventory)
