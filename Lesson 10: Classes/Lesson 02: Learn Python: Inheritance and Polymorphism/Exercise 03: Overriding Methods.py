# In Python, all we have to do to override a method definition is to offer a new definition for the method in our subclass.

# An overridden method is one that has a different definition from its parent class.

class Message:
  def __init__(self, sender, recipient, text):
    self.sender = sender
    self.recipient = recipient
    self.text = text

class User:
  def __init__(self, username):
    self.username = username
    
  def edit_message(self, message, new_text):
    if message.sender == self.username:
      message.text = new_text

# Create Admin subclass from User class
class Admin(User):
  # Override edit_message method
  def edit_message(self, message, new_text):
    # Set message.text equal to new_text
    message.text = new_text
