# Create a function named more_frequent_item that has three parameters named lst, item1, and item2.

# Return either item1 or item2 depending on which item appears more often in lst.

# If the two items appear the same number of times, return item1.

#Write your function here
def more_frequent_item(lst, item1, item2):
  # Count appearances of both items
  item1_count = lst.count(item1)
  item2_count = lst.count(item2)
  # If both items appear the same number of times
  if (item1_count == item2_count):
    # Return item1
    return item1
  # Else if item1 appears more than item2
  elif (item1_count > item2_count):
    # Return item1
    return item1
  # Else item2 appears more than item1
  else:
    # Return item2
    return item2

#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
