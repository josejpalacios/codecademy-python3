# You can stop a for loop from inside the loop by using break.
# When the program hits a break statement, control returns to the code outside of the for loop.

dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

# Create for loop
for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  # Added if statement
  if(dog_breed == dog_breed_I_want):
    print("They have the dog I want!")
    # Added break to stop loop
    break
