# Create a function called every_three_nums that has one parameter named start.

# The function should return a list of every third number between start and 100 (inclusive).
# For example, every_three_nums(91) should return the list [91, 94, 97, 100].
# If start is greater than 100, the function should return an empty list.

#Write your function here
def every_three_nums(start):
  # If start > 100
  if (start > 100):
    # Return empty list
    return []
  # Else start <= 100
  else:
    # Create list between start and 100
    new_lst = list(range(start, 101, 3))
    # Return new_lst
    return new_lst

#Uncomment the line below when your function is done
print(every_three_nums(91))
