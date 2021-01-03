# json.dump() takes two arguments: first the data object, then the file object you want to save.

# Import json
import json

data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

# Open file
with open('data.json', 'w') as data_json:
  # Write to json file
  json.dump(data_payload, data_json)
