# This is called slicing a string.
# When we slice a string we are creating a new string that
# starts at (and includes) the first_index and ends at (but excludes) the last_index.

# We can also have open-ended selections.
# If we remove the first index, the slice starts at the beginning of the string
# and if we remove the second index the slice continues to the end of the string.

first_name = "Rodrigo"
last_name = "Villanueva"

# Slicing strings
new_account = last_name[:5]
temp_password = last_name[2:6]
