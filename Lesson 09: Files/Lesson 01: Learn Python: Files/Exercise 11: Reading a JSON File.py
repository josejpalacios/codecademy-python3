# JSON, an abbreviation of JavaScript Object Notation,
# is a file format inspired by the programming language JavaScript.

# Import json module
import json

# Open file
with open('message.json') as message_json:
  # Read json file object
  message = json.load(message_json)
  # Print message
  print(message['text'])
