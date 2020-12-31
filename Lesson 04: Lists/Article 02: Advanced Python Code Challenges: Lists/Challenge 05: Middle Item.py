# Create a function called middle_element that has one parameter named lst.

# If there are an odd number of elements in lst, the function should return the middle element.
# If there are an even number of elements, the function should return the average of the middle two elements.

#Write your function here
def middle_element(lst):
  # Get size of lst
  lst_size = len(lst)
  # Divide size by 2
  middle_index = int(lst_size/2)
  # If lst size is odd
  if (lst_size % 2 == 1):
    # Get the middle element
    middle = lst[middle_index]
    # Return middle
    return middle
  # Else lst size is even
  else:
    # Get both middle elements
    middle1 = lst[middle_index]
    middle2 = lst[middle_index-1]
    # Find the average of both elements
    average = (middle1 + middle2) / 2
    # Return average
    return average

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))
