#  argument 'w' to open() in order to indicate to open the file in write-mode.
# The default argument is 'r' and passing 'r' to open() opens the file in read-mode as we’ve been doing.

# It’s important to note that if there is already a file called generated_file.txt
# it will completely overwrite that file, erasing whatever its contents were before.

# Open file
with open('bad_bands.txt', 'w') as bad_bands_doc:
  # Write to file
  bad_bands_doc.write('Bad Band')
