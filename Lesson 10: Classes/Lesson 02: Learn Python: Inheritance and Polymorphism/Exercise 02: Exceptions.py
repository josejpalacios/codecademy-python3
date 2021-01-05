# An Exception is a class that inherits from Python’s Exception class.

# issubclass() is a Python built-in function that takes two parameters. 
# issubclass() returns True if the first argument is a subclass of the second argument.
# It returns False if the first class is not a subclass of the second.
# issubclass() raises a TypeError if either argument passed in is not a class.

# Define your exception up here:
class OutOfStock(Exception):
  # Message
  """
  Exception for the color is out of stock
  """

# Update the class below to raise OutOfStock
class CandleShop:
  name = "Here's a Hot Tip: Buy Drip Candles"
  def __init__(self, stock):
    self.stock = stock
    
  def buy(self, color):
    # If stock of color is 0
    if (self.stock[color] == 0):
      # Raise OutOfStock
      raise OutOfStock
    # Else color is in stock
    else:
      # Reduce stock of color by 1
      self.stock[color] = self.stock[color] - 1

candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
candle_shop.buy('blue')

# This should raise OutOfStock:
try:
  candle_shop.buy('green')
except OutOfStock:
  print("This item is out of stock.")
