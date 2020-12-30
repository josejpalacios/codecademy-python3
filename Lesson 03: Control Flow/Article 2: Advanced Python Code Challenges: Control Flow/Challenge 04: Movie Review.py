# Create a function named movie_review() that has one parameter named rating.

# If rating is less than or equal to 5, return "Avoid at all costs!".
# If rating is between 5 and 9, return "This one was fun.".
# If rating is 9 or above, return "Outstanding!"

# Write your movie_review function here:
def movie_review(rating):
  # If rating >= 9
  if (rating >=9):
    # Return message
    return "Outstanding!"
  # Else if rating > 5 and rating < 9
  elif (rating > 5) and (rating < 9):
    # Return message
    return "This one was fun."
  # Else rating <= 5
  else:
    # Return message
    return "Avoid at all costs!"

# Uncomment these function calls to test your movie_review function:
print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."
