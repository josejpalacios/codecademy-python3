# You can get both the keys and the values with the .items() method.
# Like .keys() and .values(), it returns a dict_list object.
# Each element of the dict_list returned by .items() is a tuple consisting of:
# (key, value)

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}
# Iterate through dictionary
for key, value in pct_women_in_occupation.items():
  # Print message
  print("Women make up {value} percent of {key}s.".format(value=value, key=key))
