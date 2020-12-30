# A second way of sorting a list is to use sorted.

# sorted is different from .sort() in several ways:
# - It comes before a list, instead of after.
# - It generates a new list.

games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']

# Create new sorted list
games_sorted = sorted(games)
print(games)
# games remained unsorted
print(games_sorted)
# games_sorted is sorted
