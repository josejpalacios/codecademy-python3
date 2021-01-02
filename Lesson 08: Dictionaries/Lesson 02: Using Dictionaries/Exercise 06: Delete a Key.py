# .pop() works to delete items from a dictionary, when you know the key value.

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20
# Add value of stamina grains, 0 if not found, to health points and remove from dictionary
health_points += available_items.pop("stamina grains", 0)
# Add value of power stew, 0 if not found, to health points and remove from dictionary
health_points += available_items.pop("power stew", 0)
# Add value of mystic bread, 0 if not found, to health points and remove from dictionary
health_points += available_items.pop("mystic bread", 0)
# Print available_items and health_points
print(available_items)
print(health_points)
