# Write a function named append_sum that has one parameter — a list named named lst.

# The function should add the last two elements of lst together and append the result to lst.
# It should do this process three times and then return lst.

# For example, if lst started as [1, 1, 2], the final result should be [1, 1, 2, 3, 5, 8].

#Write your function here
def append_sum(lst):
  # Add last two elements together
  add_last_two = lst[-1] + lst[-2]
  # Append result to lst
  lst.append(add_last_two)
  # Add last two elements together
  add_last_two = lst[-1] + lst[-2]
  # Append result to lst
  lst.append(add_last_two)
  # Add last two elements together
  add_last_two = lst[-1] + lst[-2]
  # Append result to lst
  lst.append(add_last_two)
  # Return lst
  return lst

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))
