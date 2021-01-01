# .format() can be made even more legible for other
# people reading your code by including keywords. 

# By including keywords in the string and in the arguments,
# you can remove that ambiguity.

# Fix format method
def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc

# Call poem_description
author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"
my_beard_description = poem_description(publishing_date, author, title, original_work)
