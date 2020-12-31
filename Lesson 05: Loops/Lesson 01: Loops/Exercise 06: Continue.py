# We can use continue to move to the next iteration in a loop

# The continue keyword moves the counter to the next value, without executing the code in the rest of the for loop.
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

# Loop through ages
for age in ages:
  # If age is less than 21
  if (age < 21):
    # Skip and move to next value
    continue
  # Else
  else:
    # Print age
    print(age)
