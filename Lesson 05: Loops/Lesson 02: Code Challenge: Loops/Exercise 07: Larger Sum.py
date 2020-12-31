# Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.

# The function should return the list whose elements sum to the greater number.
# If the sum of the elements of each list are equal, return lst1.

#Write your function here
def larger_sum(lst1, lst2):
  # Create two variables to store sums
  lst1_sum = 0
  lst2_sum = 0
  # Iterate through lst1
  for num in lst1:
    # Add number to lst1_sum
    lst1_sum += num
  # Iterate through lst2
  for num in lst2:
    # Add number to lst2_sum
    lst2_sum += num
  # If both sums are equal
  if (lst1_sum == lst2_sum):
    # Return lst1
    return lst1
  # Else if lst1_sum is greater
  elif (lst1_sum > lst2_sum):
    # Return lst
    return lst1
  # Else lst2_sum is greater
  else:
    # Return lst2
    return lst2
  
#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))
