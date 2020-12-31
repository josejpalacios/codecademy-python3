heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

# Create list using list comprehension
can_ride_coaster = [height for height in heights if height > 161]
# This list comprehension:
# - Takes an element in heights
# - Assigns that element to a variable called height
# - Checks if height > 161, and if so, it adds height to the new list, can_ride_coaster. If not, nothing happens.
# - Repeats steps for all numbers in heights

print(can_ride_coaster)
