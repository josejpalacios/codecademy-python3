# When we call a function in Python, we need to list the arguments to that function to
# match the order of the parameters in the function definition.

# We don’t necessarily need to do this if we pass keyword arguments.

# We use keyword arguments by passing arguments to a function with a
# special syntax that uses the names of the parameters.

# This is useful if the function has many optional default arguments
# or if the order of a function’s parameters is hard to tell. 

import shapes

def draw_shape(shape_name="box", character="x", line_breaks=True):
  shape = shapes.draw_shape(shape_name, character)
  if not line_breaks:
    print(shape[1:-1])
  else:
    print(shape)

# call draw_shape() with keyword arguments here:
draw_shape(character='m', line_breaks=False)
