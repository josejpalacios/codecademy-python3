first_name = "Julie"
last_name = "Blevins"

# Write account_generator function
def account_generator(first_name, last_name):
  # Get first three letters
  first = first_name[:3]
  last = last_name[:3]
  # Concatenate strings
  new_account = first + last
  # Return new_account
  return new_account

# Call account_generator
new_account = account_generator(first_name, last_name)
