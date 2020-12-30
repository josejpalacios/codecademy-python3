# Create get_boundaries with two parameters, target and margin
def get_boundaries(target, margin):
  # Create variable low_limit
  low_limit = target - margin
  # Create variable high_limit
  high_limit = margin + target

  # Return low_limit and high_limit
  return low_limit, high_limit

# Call get_boundaries with:
# target: 100
# margin: 20
# Save values to low and high
low, high = get_boundaries(100, 20)
