# Dictionaries have a .values() method that returns a dict_values object
# (just like a dict_keys object but for values!) with all of the values in the dictionary.

# It can be used in the place of a list for iteration.

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
# Create total_exercises
total_exercises = 0
# Iterate through num_exercises
for num in num_exercises.values():
  # Add number to total_exercises
  total_exercises += num
# Print total_exercises
print(total_exercises)
