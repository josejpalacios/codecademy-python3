# A for loop lets us perform an action on each item in a list.
# Using each element of a list is known as iterating.

# Structure for loop
# for <temporary variable> in <list variable>:
#     <action>

# The temporary variable can be named whatever we want and does not need to be defined beforehand.

# Everything in the same level of indentation after the for loop declaration
# is included in the for loop, and run every iteration.

# If we forget to indent, we’ll get an IndentationError.

board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']

sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']

for game in board_games:
# IndentationError: expected an indented block
#print(game)
  # Fixed IndentationError
  print(game)

# Create for loop
for sport in sport_games:
  print(sport)
