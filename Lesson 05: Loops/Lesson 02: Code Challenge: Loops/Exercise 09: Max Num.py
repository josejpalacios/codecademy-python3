# Create a function named max_num() that takes a list of numbers named nums as a parameter.

# The function should return the largest number in nums

#Write your function here
def max_num(nums):
  # Create variable to hold largest number
  largest = nums[0]
  # Iterate through nums
  for num in nums:
    # If num > largest
    if (num > largest):
      # Set largest equal to num
      largest = num
  # Return largest
  return largest


#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))
