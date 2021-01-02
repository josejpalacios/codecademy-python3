# Cannot use list or a dictionary as keys
# Results in TypeError: unhashable type: 'list'

# The word “unhashable” in this context means that this ‘list’ is an object that can be changed.
# Dictionaries in Python rely on each key having a hash value, a specific identifier for the key.
# If the key can change, that hash value would not be reliable.
# So the keys must always be unchangeable, hashable data types, like numbers or strings.

# Swapped keys and values
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"], "Corleone": ["Sonny", "Fredo", "Michael"]}
