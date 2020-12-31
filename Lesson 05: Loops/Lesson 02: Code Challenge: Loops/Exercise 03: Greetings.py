# Create a function named add_greetings() which takes a list of strings named names as a parameter.

# In the function, create an empty list that will contain each greeting.
# Add the string "Hello, " in front of each name in names and append the greeting to the list.

# Return the new list containing the greetings.

#Write your function here
def add_greetings(names):
  # Create empty_list
  greetings = []
  # Iterate through names
  for name in names:
    # Add Hello
    greeting = "Hello, " + name
    # Append greeting to greetings
    greetings.append(greeting)
  # Return greetings
  return greetings

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))
