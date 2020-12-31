# Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.

# Return the count of how many numbers in the list are divisible by 10.

#Write your function here
def divisible_by_ten(nums):
  # Create variable count
  count = 0
  # Iterate through nums
  for num in nums:
    # If num is divisible by 10
    if (num % 10 == 0):
      # Increment count by 1
      count += 1
  # Return count
  return count

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))
