# .update() - add multiple key : value pairs to a dictionary at once

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

# Add using update()
user_ids.update({
  "theLooper": 138475,
  "stringQueen": 85739
})
# Print dictionary
print(user_ids)
