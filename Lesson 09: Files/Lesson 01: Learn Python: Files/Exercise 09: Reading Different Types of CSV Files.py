# WIth csv.DictReader we can pass in the delimiter parameter,
# which is the string that’s used to delineate separate fields in the CSV.

# Import csv module
import csv

# Open file
with open('books.csv') as books_csv:
  # Create csv dictionary
  books_reader = csv.DictReader(books_csv, delimiter='@')
  # Create list
  isbn_list = []
  # Iterate csv dictionary
  for isbn in books_reader:
    # Append ISBN info to isbn_list
    isbn_list.append(isbn['ISBN'])
