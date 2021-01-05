# __init__(), the constructor, use to setup instance variables

# __iter__, the iterator, allows to us for element in list

# __len__, the length method, use to call len(user_group)

# __contains__, the check for containment, allows to us if element in elements

class LawFirm:
  def __init__(self, practice, lawyers):
    self.practice = practice
    self.lawyers = lawyers

  # Create __len__() dunder method
  def __len__(self):
    # returh length of lawyers
    return len(self.lawyers)

  # Create __contains__() dunder method
  def __contains__(self, lawyer):
    # If lawyer in self.lawyers
    if (lawyer in self.lawyers):
      # Return True
      return True
    # Else lawyer is not in self.lawyers
    else:
      # Return False
      return False
    
d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])
