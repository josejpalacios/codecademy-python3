# Write a function named larger_list that has two parameters named lst1 and lst2.

# The function should return the last element of the list that contains more elements.
# If both lists are the same size, then return the last element of lst1.

#Write your function here
def larger_list(lst1, lst2):
  # Get length of both list
  lst1_len = len(lst1)
  lst2_len = len(lst2)

  # If both list are the same size
  if (lst1_len == lst2_len):
    # Return last element of lst1
    return lst1[-1]
  # Else if lst1 is larger
  elif (lst1_len > lst2_len):
    #  Return last element of lst1
    return lst1[-1]
  # Else lst2 is larger
  else:
    # Return last element of lst2
    return lst2[-1]

#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))
