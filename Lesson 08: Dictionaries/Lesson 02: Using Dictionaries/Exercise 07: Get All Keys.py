# The built-in list() function gets all the keys of the dictionary

# Dictionaries also have a .keys() method that returns a dict_keys object.

# A dict_keys object is a view object, which provides a look at the current state of the dictionary,
# without the user being able to modify anything.

# The dict_keys object returned by .keys() is a set of the keys in the dictionary.

# You cannot add or remove elements from a dict_keys object,
# but it can be used in the place of a list for iteration

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
# Create dict_keys object
users = user_ids.keys()
# Create dict_keys object
lessons = num_exercises.keys()
# Print users
print(users)
# Print lessons
print(lessons)
