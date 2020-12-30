# zip takes two (or more) lists as inputs and returns an object that contains a list of pairs.

# Each pair contains one element from each of the inputs.

# You will have to convert zip object to list in order to print the nested lists

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']

# Create zip object
names_and_dogs_names = zip(names, dogs_names)

# Convert zip object to list
list_names_and_dogs_names = list(names_and_dogs_names)

# Print list
print(list_names_and_dogs_names)
