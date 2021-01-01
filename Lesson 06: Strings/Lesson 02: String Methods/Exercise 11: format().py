# .format() takes variables as an argument and
# includes them in the string that it is run on.
# You include {} marks as placeholders for where
# those variables will be imported.

# .format() can take as many arguments as there are {} in the string it is run on.

# Write poem_title_card function
def poem_title_card(title, poet):
  # Return string using format
  return "The poem \"{}\" is written by {}.".format(title, poet)
