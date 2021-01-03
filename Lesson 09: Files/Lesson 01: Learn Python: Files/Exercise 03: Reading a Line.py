# .readline(), which will only read a single line at a time.

# Open file
with open('just_the_first.txt') as first_line_doc:
  # Save first line
  first_line = first_line_doc.readline()
# Print first_line
print(first_line)
