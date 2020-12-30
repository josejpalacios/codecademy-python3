# Create function repeat_stuff
# Inputs: stuff, num_repeats=10
def repeat_stuff(stuff, num_repeats=10):
  # Return stuff * num_repeats
  return stuff * num_repeats

# Call repeat_stuff with:
# stuff: Row 
# num_repeats: 3
# Store value to lyrics
lyrics = repeat_stuff("Row ", 3) + "Your Boat. "

# Call repeat_stuff with:
# stuff: lyrics (Variable)
# Store value to song
song = repeat_stuff(lyrics)

# Print song
print(song)
