# The keyword argument unpacking syntax can be used
# even if the function takes other parameters.
# However, the parameters must be listed in this order:
# - All named positional parameters
# - An unpacked positional parameter (*args)
# - All named keyword parameters
# - An unpacked keyword parameter (**kwargs)

def remove(filename, *args, **kwargs):
  with open(filename) as file_obj:
    text = file_obj.read()

  # Add code here to update text.
  for arg in args:
    print(arg)
    # Use replace() and store in variable
    text = text.replace(arg, '')
  # Iterate through kwargs
  for kwarg, replacement in kwargs.items():
    # Use replace and store in variable
    text = text.replace(kwarg, replacement)
  
  return text

print(remove("text.txt", "generous", "gallant", fond="amused by", Robin="Mr. Robin"))
