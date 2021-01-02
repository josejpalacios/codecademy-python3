# When we try to access a key that doesn’t exist,
# the program will go into the except block and print "That key doesn't exist!".

caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120, "matcha": 30}
# Use try and except to print
try:
  print(caffeine_level["matcha"])
except KeyError:
  print("Unknown Caffeine Level") 
