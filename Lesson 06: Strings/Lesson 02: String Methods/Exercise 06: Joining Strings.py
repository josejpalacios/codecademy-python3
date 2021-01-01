# .join() is essentially the opposite of .split(),
# it joins a list of strings together with a given delimiter.

# .join() is still a string method, which means it has to act on a string.
# The string .join() acts on is the delimiter you want to join with,
# therefore the list you want to join has to be the argument.

reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

# Use .join()
reapers_line_one = ' '.join(reapers_line_one_words)
