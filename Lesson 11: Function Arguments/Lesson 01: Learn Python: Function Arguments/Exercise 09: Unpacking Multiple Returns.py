# A Python function can return multiple things. 

# In Python we can return multiple pieces of data by separating each variable with a comma

# tuple is an immutable list-like object indicated by parentheses.

def scream_and_whisper(text):
    scream = text.upper()
    whisper = text.lower()
    return scream, whisper

# Call scream_and_whisper and unpack return values into two variables
the_scream, the_whisper = scream_and_whisper('Hello')
