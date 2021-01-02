# If a variable is defined inside of a function, it will not be accessible outside of the function.

# Scope also applies to classes and to the files you are working within.

# Files are actually modules, so you can give a file access to another file’s content using the import statement.

# ==============
# script.py File
# ==============
# Import library below:
from library import always_three


# Call your function below:
# NameError: name 'always_three' is not defined | Before adding import statement
always_three()

# ==========
# library.py
# ==========
# Add your always_three() function below:
def always_three():
  # Return 3
  return 3
