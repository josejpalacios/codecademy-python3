# Starting code
from nile import get_distance, format_price, SHIPPING_PRICES
from test import test_function

# =================================
# Not Just A River In Egypt Section
# =================================
# Task 1: Define calculate_shipping_cost() here:
# Task 7 Code
def calculate_shipping_cost(from_coords, to_coords, shipping_type='Overnight'):
  # Task 2: Unpack from_coords and to_coords tuples
  from_lat, from_long = from_coords[0], from_coords[1]
  # Unpack to_coords tuple
  to_lat, to_long = to_coords[0], to_coords[1]
  # Task 3: Call get_distance
  distance = get_distance(from_lat, from_long, to_lat, to_long)
  # Task 4: Create variable shipping_rate using SHIPPING_PRICES and shipping_type
  shipping_rate = SHIPPING_PRICES[shipping_type]
  # Task 5: Calculate price
  price = distance * shipping_rate
  # Task 6: Return formatted price
  return format_price(price)

# Task 7: Make shipping_type a default parameter with the value 'Overnight'. Code is above at Task 7 Code

# Task 8: Test the function by calling 
test_function(calculate_shipping_cost)

# ===========================
# Careers At The Nile Section
# ===========================
# Task 9: Define calculate_driver_cost() here
def calculate_driver_cost(distance, *drivers):
  # Task 10: Create cheapest_driver and cheapest_driver_price variables. Set both to None
  cheapest_driver = None
  cheapest_driver_price = None
  # Task 11: Iterate through drivers
  for driver in drivers:
    # Task 12: Calculate driver_time
    driver_time = driver.speed * distance
    # Task 13: Calculate price_for_driver
    price_for_driver = driver.salary * driver_time
    # Task 14: Check if current driver is the cheapest driver
    if (cheapest_driver is None):
      # Set values to cheapest_driver and cheapest_driver_price
      cheapest_driver = driver
      cheapest_driver_price = price_for_driver
    # Task 15: Add else if statement to check if price_for_driver is less than cheapest_driver_price
    elif (price_for_driver < cheapest_driver_price):
      # Update values for cheapest_driver and cheapest_driver_price
      cheapest_driver = driver
      cheapest_driver_price = price_for_driver
  # Task 16: Return cheapest_driver and cheapest_driver_price
  return cheapest_driver_price, cheapest_driver

# Test the function by calling 
test_function(calculate_driver_cost)

# ==========================
# The Nile Exclusive Section
# ==========================
# Task 17: Define calculate_money_made() here
def calculate_money_made(**trips):
  # Task 18: Create total_money_made variable
  total_money_made = 0
  # Task 19: Iterate through trips
  for trip_id, trip in trips.items():
    # Task 20: Calculate trip_revenue
    trip_revenue = trip.cost - trip.driver.cost
    # Task 21: Add trip_revenue to total_money_made
    total_money_made += trip_revenue
  # Task 22: Return total_money_made
  return total_money_made
  
# Task 23: Test the function by calling
test_function(calculate_money_made)
