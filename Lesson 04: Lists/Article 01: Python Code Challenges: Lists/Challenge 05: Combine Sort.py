# Write a function named combine_sort that has two parameters named lst1 and lst2.

# The function should combine these two lists into one new list and sort the result.
# Return the new sorted list.

#Write your function here
def combine_sort(lst1, lst2):
  # Create new list using lst1 and lst2
  new_lst = lst1 + lst2
  # Sort new list
  new_lst.sort()
  # Return new list sorted
  return new_lst

#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
