# ========================
# Making the Menus Section
# ========================
# Task 1: Create Menu class
class Menu:
  # Task 2: Create constructor with five parameters: self, name, items, start_time, and end_time
  def __init__(self, name, items, start_time, end_time):
    # Create instance variables
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  # Task 7 Code
  def __repr__(self):
    # Return message
    return "Menu Name: {name}\nStart Time: {start}\nEnd Time: {end}".format(name=self.name, start=self.start_time, end=self.end_time)
  # Task 9 Code
  def calculate_bill(self, purchased_items):
    # Create total_bill
    total_bill = 0
    # Iterate through purchased_items
    for purchased_item in purchased_items:
      # Add value to total_bill
      total_bill += self.items[purchased_item]
    # Return total_bill
    return total_bill

# Task 3: Create Menu object
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
# Create object
brunch = Menu('Brunch', brunch_items, 11, 16)

# Task 4: Create another Menu object
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
# Create object
early_bird = Menu('Early Bird', early_bird_items, 15, 18)

# Task 5: Create third Menu object
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
# Create object
dinner = Menu('Dinner', dinner_items, 17, 23)

# Task 6: Create last Menu object
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
# Create object
kids = Menu('Kids', kids_items, 11, 21)

# Task 7: Add string representation dunder method to Menu Class. Code is above at Task 7: Code

# Task 8: Test string representation method
print(brunch)

# Task 9: Create calculate_bill in Menu class. Has two parameters, self and purchased_items, list of items purchased. Return the total cost of the items purchased. Code is above at Task 9 Code.

# Task 10: Test calculate_bill method and print result. Should be 13.5
breakfast_order = ['pancakes', 'home fries', 'coffee']
# Call calculate_bill method.
print(brunch.calculate_bill(breakfast_order))

# Task 11: Test calculate_bill on early_bird object and print result. Should be 21.5
early_bird_order = ['salumeria plate', 'mushroom ravioli (vegan)']
print(early_bird.calculate_bill(early_bird_order))

# ===============================
# Creating the Franchises Section
# ===============================
# Task 12: Create Franchise class
class Franchise:
  # Task 13: Create constructor with three parameters self, address and menus
  def __init__(self, address, menus):
    # Create instance variables
    self.address = address
    self.menus = menus
  # Task 15 Code
  def __repr__(self):
    # Return message
    return 'Address of restaurant is {address}'.format(address=self.address)
  # Task 16 Code
  def available_menus(self, time):
    # Create empty list
    available_menus_at_time = []
    # Iterate through list of menus
    for menu in self.menus:
      # If time > start_time and time < end_time
      if ( (time >= menu.start_time) and (time < menu.end_time) ):
        # Append menu to available_menus_at_time
        available_menus_at_time.append(menu)
    # Return available_menus_at_time
    return available_menus_at_time



# Task 14: Create two Franchise objects. Use previously created Menu objects
menus = [brunch, early_bird, dinner, kids]
# Create first Franchise object
flagship_store = Franchise('1232 West End Road', menus)
# Create second Franchise object
new_installment = Franchise('East Mulberry Street', menus)

# Task 15: Add string representation to Franchise class. Code is above at Task 15 Code
# Test __repr__ method
print(flagship_store)

# Task 16: Create available_menus method. Takes two parameters, self and time, and returns a list of Menu objects that are available at the time. Code is above at Task 16 code.

# Task 17: Test available_menus method with 12 as an argument and print results. Should return Brunch and Kids
print(flagship_store.available_menus(12))

# Task 18: Test again with 17 as an input and print results. Should return Early Bird, Dinner and Kids
print(flagship_store.available_menus(17))

# ============================
# Creating Businesses! Section
# ============================
# Task 19: Create Business class
class Business:
  # Task 20: Add constructor
  def __init__(self, name, franchises):
    # Create instance variables
    self.name = name
    self.franchises = franchises

# Task 21: Create Business object
franchises = [flagship_store, new_installment]
business = Business('Basta Fazoolin'' with my Heart', franchises)

# Task 22: Create new Menu object
arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
# Create Menu object
arepas_menu = Menu('Take a’ Arepa', arepas_items, 10, 20)

# Task 23: Create new Franchise object
arepas_menus = [arepas_menu]
# Create Franchise object
arepas_place = Franchise('189 Fitzgerald Avenue', arepas_menus)

# Task 24: Create new Business object
arepas_business = Business('Take a\' Arepa', arepas_place)

# Task 25 and 26: Finished Project
