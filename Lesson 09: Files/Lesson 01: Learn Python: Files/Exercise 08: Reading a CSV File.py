# In Python we can convert CSV data into a dictionary using the csv library’s DictReader object.

# csv.DictReader(users_csv) converts the lines of a CSV file to Python dictionaries which we can be used for later.
# The keys of the dictionary are, by default, the entries in the first line of our CSV file.

# Import csv module
import csv

# Open file using with
with open('cool_csv.csv') as cool_csv_file:
  # Read csv into dictionary
  cool_csv_dict = csv.DictReader(cool_csv_file)
  # Iterate through csv dictionary
  for row in cool_csv_dict:
    # Print Cool Fact
    print(row["Cool Fact"])
