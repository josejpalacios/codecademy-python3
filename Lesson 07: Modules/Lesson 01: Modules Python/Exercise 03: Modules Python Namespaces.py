# A namespace isolates the functions, classes, and variables defined
# in the module from the code in the file doing the importing.
# Your local namespace, meanwhile, is where your code is run.

# Aliasing (as) is most often done if the name of the library is
# long and typing the full name every time you want to use one of its functions is laborious.

# The * is known as a “wildcard” and matches anything and everything.
# This syntax is considered dangerous because it could pollute our local namespace.
# Pollution occurs when the same name could apply to two possible things.

# random.sample() takes a range and a number as its arguments.
# It will return the specified number of random numbers from that range.

import codecademylib3_seaborn
# Add your code below:
from matplotlib import pyplot as plt
import random
# Create range variables
numbers_a = range(1, 13)
numbers_b = random.sample(range(1000), 12)
# Plot sets
plt.plot(numbers_a, numbers_b)
# Show plot
plt.show()
