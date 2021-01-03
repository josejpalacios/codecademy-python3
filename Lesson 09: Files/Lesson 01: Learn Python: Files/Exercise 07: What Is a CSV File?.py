# CSV files are an example of a text file that impose a structure to their data.

# CSV stands for Comma-Separated Values and CSV files are usually the way
# that data from spreadsheet software (like Microsoft Excel or Google Sheets)
# is exported into a portable format.

# Open file using with
with open('logger.csv') as log_csv_file:
  # Print contents of file
  print(log_csv_file.read())
