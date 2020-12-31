sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

# Create scoops_sold
scoops_sold = 0

# Nest for loop
for location in sales_data:
  # Inner loop
  for scoop in location:
    # Add scoop to scoops_sold
    scoops_sold += scoop

print(scoops_sold)
