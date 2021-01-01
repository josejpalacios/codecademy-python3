# .strip() removes all whitespace characters from the beginning and end.

# You can also use .strip() with a character argument,
# which will strip that character from either end of the string.

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

# Strip whitespace
love_maybe_lines_stripped= [line.strip() for line in love_maybe_lines]

# Join lines
love_maybe_full = "\n".join(love_maybe_lines_stripped)

# Print lines
print(love_maybe_full)
