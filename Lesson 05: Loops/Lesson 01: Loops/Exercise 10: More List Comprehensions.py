celsius = [0, 10, 15, 32, -5, 27, 3]

fahrenheit = [temp * 9/5 + 32 for temp in celsius]
# Takes a number in celsius
# - Assigns value to temp
# - Converts number to fahrenheit
# - Appends value to fahrenheit list
# Repeats steps for all numbers in celsius

print(fahrenheit)
