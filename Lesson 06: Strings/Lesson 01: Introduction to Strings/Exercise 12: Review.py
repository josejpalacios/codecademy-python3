# Write username_generator function
def username_generator(first_name, last_name):
  # Variable to store username
  username = ""
  # If first_name < 3
  if (len(first_name) < 3):
    # Add first_name to username
    username += first_name
  # Else first_name > 3
  else:
    # Add first three letters of first_name to username
    username += first_name[:3]
  # if last_name < 4
  if (len(last_name) < 4):
    # Add last_name to username
    username += last_name
  # Else last_name > 4
  else:
    # Add first four letters of last_name to username
    username += last_name[:4]
  # Return username
  return username

# Write password_generator function
def password_generator(username):
  # Create empty string
  password = ""
  # Iterate through username indices
  for index in range(0, len(username)):
    # Add previous letter to password
    password += username[index-1]
  # Return password
  return password
