# We can also split strings using escape sequences.
# Escape sequences are used to indicate that we want
# to split by something in a string that is not necessarily a character.

# Escape sequences
# \n Newline
# \t Horizontal Tab

spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

# Split use \n
spring_storm_lines = spring_storm_text.split('\n')
