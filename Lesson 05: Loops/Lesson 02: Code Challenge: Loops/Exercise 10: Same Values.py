# Write a function named same_values() that takes two lists of numbers of equal size as parameters.

# The function should return a list of the indices where the values were equal in lst1 and lst2.

# For example, the following code should return [0, 2, 3]

# same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])

#Write your function here
def same_values(lst1, lst2):
  # Create empty list
  indices = []
  # Iterate through both list
  for index in range(0, len(lst1)):
    # If element at index is the same in both list
    if (lst1[index] == lst2[index]):
      # Append index to indices
      indices.append(index)
  # Return list created
  return indices

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
