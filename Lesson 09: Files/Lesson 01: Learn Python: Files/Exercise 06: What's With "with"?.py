# The with keyword invokes something called a context manager for the file that we’re calling open() on.
# This context manager takes care of opening the file when we call open() and then closing the file after we leave the indented block.

# All the variables you create: integers, lists, dictionaries
# — these are all Python objects, and Python knows how to clean them up when it’s done with them.

# Since your files exist outside your Python script,
# we need to tell Python when we’re done with them
# so that it can close the connection to that file.

# Leaving a file connection open unnecessarily can affect performance
# or impact other programs on your computer that might be trying to access that file.

# The with syntax replaces older ways to access files
# where you need to call .close() on the file object manually.

# We can still open up a file and append to it with the old syntax,
# as long as we remember to close the file connection afterwards.

# Since this is necessarily more verbose (requires at least one more line of code)
# without being any more expressive, using with is preferred.

# Open file manually
# close_this_file = open('fun_file.txt')
# Open file using with
with open('fun_file.txt') as close_this_file:
  # Read lines
  setup = close_this_file.readline()
  punchline = close_this_file.readline()
