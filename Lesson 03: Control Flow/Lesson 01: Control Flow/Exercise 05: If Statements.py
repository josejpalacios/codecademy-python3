def dave_check(user_name):
  # Fixed SyntaxError = to ==
  if user_name == "Dave":
    return "Get off my computer Dave!"
  # Added second if statement
  if user_name == "angela_catlady_87":
    return "I know it is you Dave! Go away!"

  
# Enter a user name here, make sure to make it a string
user_name = "Jose"

print(dave_check(user_name))
