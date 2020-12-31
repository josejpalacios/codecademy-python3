# Create a function named more_than_n that has three parameters named lst, item, and n.

# The function should return True if item appears in the list more than n times.
# The function should return False otherwise.

#Write your function here
def more_than_n(lst, item, n):
  # Count appearance of item in lst
  appearances = lst.count(item)
  # If appearances of item > n
  if (appearances > n):
    # Return True
    return True
  # Else appearances of item <= n
  else:
    # Return False
    return False

#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))
