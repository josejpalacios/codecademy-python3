# .read()grabs the whole document in a single string
# .readlines() reads a text file line by line

# Open file
with open('how_many_lines.txt') as lines_doc:
  # Iterate through lines of file
  for line in lines_doc.readlines():
    # Print line
    print(line)
