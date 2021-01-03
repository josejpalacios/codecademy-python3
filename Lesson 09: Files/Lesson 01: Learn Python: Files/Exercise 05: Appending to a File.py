# open with 'a' for append-mode.

# Notice that opening the file in append-mode, with 'a' as an argument to open(),
# means that using the file object’s .write() method appends whatever is passed to the end of the file in a new line.

# Open file
with open('cool_dogs.txt', 'a') as cool_dogs_file:
  # Add line of text
  cool_dogs_file.write("Air Buddy")
