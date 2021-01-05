# Not only can we accept arbitrarily many parameters to a function in our definition,
# but Python also supports a syntax that makes deconstructing any data that you have on hand
# to feed into a function that accepts these kinds of unpacked arguments.

# The syntax is very similar, but is used when a function is called, not when it’s defined.

# We can use the * when calling the function that takes a series of
# positional parameters to unwrap a list or a tuple.

# This makes it easy to provide a sequence of arguments to a function
# even if that function doesn’t take a list as an argument.

# Similarly we can use ** to destructure a dictionary.

from products import create_product

def create_products(**products_dict):
  for name, price in products_dict.items():
    create_product(name, price)

new_product_dict = {
  'Apple': 1,
  'Ice Cream': 3,
  'Chocolate': 5,
}

# Call create_products() by passing new_product_dict
# as kwargs!
create_products(**new_product_dict)
