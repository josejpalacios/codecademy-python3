# Create a function named count_first_letter that takes a dictionary named names as a parameter.
# names should be a dictionary where the key is a last name and the value is a list of first names.
# For example, the dictionary might look like this:

# names = {"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}
# The function should return a new dictionary where each key is the first letter of a last name,
# and the value is the number of people whose last name begins with that letter.

# So in example above, the function would return:

# {"S" : 4, "L": 3}

# Write your count_first_letter function here:
def count_first_letter(names):
  # Create empty dictionary
  count_letters = {}
  # Iterate through names items
  for last_name, first_names in names.items():
    # If first letter of last_name is not in count_letters dictionary
    if (last_name[0] not in count_letters):
      # Add key value pair to count_letters
      count_letters[last_name[0]] = len(first_names)
    # Else first letter of last_name is in count_letters dictionary
    else:
      # Add value to key
      count_letters[last_name[0]] += len(first_names)
  # Return count_letters
  return count_letters

# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}
