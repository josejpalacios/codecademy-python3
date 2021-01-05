# Python gives us two methods of unpacking arguments provided to functions.
# The first method is called positional argument unpacking, because it unpacks arguments given by position. 

# We use a single asterisk (*) to indicate we’ll accept any number of positional arguments passed to the function.
# Our parameter args is a tuple of all of the arguments passed. 

# We can also have other positional parameters before our *args parameter.

# The Python library os.path has a function called join(). join() takes an arbitrary number of paths as arguments.

from os.path import join

path_segment_1 = "/Home/User"
path_segment_2 = "Codecademy/videos"
path_segment_3 = "cat_videos/surprised_cat.mp4"

# join all three of the paths here!
print(join(path_segment_1, path_segment_2, path_segment_3))

# Create myjoin function
def myjoin(*args):
  # Create join_string variable
  join_string = ""
  # Iterate through args
  for arg in args:
    # Add arg to join_string
    join_string += arg
  # Return join_string
  return join_string
