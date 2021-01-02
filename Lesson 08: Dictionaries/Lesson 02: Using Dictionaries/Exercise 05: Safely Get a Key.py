# Dictionaries have a .get() method to search for a value instead of the my_dict[key] notation we have been using.
# If the key you are trying to .get() does not exist, it will return None by default.

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
# Use get() for teraCoder, default to 100000 if not found
tc_id = user_ids.get("teraCoder", 100000)
# Print tc_id
print(tc_id)
# Use get for superStackSmash, default to 100000 if not found
stack_id = user_ids.get("superStackSmash", 100000)
# print stack_id
print(stack_id)
