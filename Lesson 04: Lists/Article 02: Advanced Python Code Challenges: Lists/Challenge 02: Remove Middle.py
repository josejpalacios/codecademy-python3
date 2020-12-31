# Create a function named remove_middle which has three parameters named lst, start, and end.

# The function should return a list where all elements in lst with an index between start and end (inclusive) have been removed.

# For example, the following code should return [4, 23, 42] because elements at indices 1, 2, and 3 have been removed:

# remove_middle([4, 8 , 15, 16, 23, 42], 1, 3)

#Write your function here
def remove_middle(lst, start, end):
  # Slice from first element to start
  lst_start = lst[:start]
  # Slice from end+1 to last element
  lst_end = lst[end+1:]
  # Add both list together
  new_lst = lst_start + lst_end
  # Return new list
  return new_lst

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
