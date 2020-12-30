# Create a function called max_num() that has three parameters named num1, num2, and num3.

# The function should return the largest of these three numbers.
# If any of two numbers tie as the largest, you should return "It's a tie!".

# Write your max_num function here:
def max_num(num1, num2, num3):
  # If num1 and num2 tie as largest
  if (num1 == num2) and (num2 > num3):
    # Return message
    return "It's a tie!"
  # Else if num1 and num3 tie as largest
  elif (num1 == num3) and (num3 > num2):
    # Return message
    return "It's a tie!"
  # Else if num2 and num3 tie as largest
  elif (num2 == num3) and (num3 > 1):
    # Return message
    return "It's a tie!"
  # Else if num1 is largest
  elif (num1 > num2) and (num1 > num3):
    # Return num1
    return num1
  # Else if num2 is largest
  elif (num2 > num1) and (num2 > num3):
    # Return num2
    return num2
  # Else num3 is largest
  else:
    # Return num3
    return num3

# Uncomment these function calls to test your max_num function:
print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"
