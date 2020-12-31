# Create a function named over_nine_thousand() that takes a list of numbers named lst as a parameter.

# The function should sum the elements of the list until the sum is greater than 9000.
# When this happens, the function should return the sum.
# If the sum of all of the elements is never greater than 9000,
# the function should return total sum of all the elements.
# If the list is empty, the function should return 0.

For example, if lst was [8000, 900, 120, 5000], then the function should return 9020.

#Write your function here
def over_nine_thousand(lst):
  # Create variable lst_sum
  lst_sum = 0
  # Iterate through lst
  for num in lst:
    # If lst_sum < 9000
    if (lst_sum < 9000):
      # Add num to lst_sum
      lst_sum += num
    # Else lst_sum > 9000
    else:
      # Break out of for loop
      break
  # Return lst_sum
  return lst_sum

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))
