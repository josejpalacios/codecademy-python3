# Starting code
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# =======================
# Prices and Cuts Section
# =======================

# Task 1: Create variable total_price
total_price = 0

# Task 2: Iterate through prices and add each price to total_price
for price in prices:
  # Add price
  total_price += price

# Task 3: Calculate average of prices
average_price = total_price / len(prices)

# Task 4: Print average of prices
print(" Average Haircut Price:")
print(average_price)

# Task 5: Create new list using list comprehension
new_prices = [price - 5 for price in prices]

# Task 6: Print new prices
print(new_prices)

# ===============
# Revenue Section
# ===============
# Task 7: Create total_revenue
total_revenue = 0

# Task 8: Create for loop
for i in range(0, len(hairstyles)):
  # Task 9: Add product of prices and last_week numbers
  value = prices[i] * last_week[i]
  # Add value to total_revenue
  total_revenue += value

# Task 10: Print total_revenue
print("Total Revenue: " + str(total_revenue))

# Task 11: Find average daily revenue. Print value.
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

# Task 12: Create list using list comprehension
cuts_under_30 = [hairstyles[i] for i in range(0, len(new_prices)-1) if new_prices[i] < 30]

# Task 13: Print cuts_under_30
print(cuts_under_30)
