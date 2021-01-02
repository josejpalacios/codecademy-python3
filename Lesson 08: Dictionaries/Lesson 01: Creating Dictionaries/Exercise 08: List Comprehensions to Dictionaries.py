# Python allows you to create a dictionary using a list comprehension

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
# Create zip list
zipped_drinks = zip(drinks, caffeine)
# Create dicitionary using list comprehension
drinks_to_caffeine = {key:value for key, value in zipped_drinks}
# Takes a pair from the zipped list of pairs from zipped_drinks
# Names the elements in the pair:
# - key (the one originally from the names drinks)
# - value (the one originally from the caffeine list)
# Creates a key : value item in the drinks_to_caffeine dictionary
# Repeats steps for the entire list of pairs
