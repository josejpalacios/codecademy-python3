# Task 1: Create description for lovely loveseat
lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""

# Task 2: Set price for lovely loveseat
lovely_loveseat_price = 254.00

# Task 3: Create description for stylish settee
stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""

# Task 4: Set price for stylish settee
stylish_settee_price = 180.50

# Task 5: Create luxurious lamp description
luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""

# Task 6: Set price for luxurious lamp
luxurious_lamp_price = 52.15

# Task 7: Set sales tax
sales_tax = 0.088

# Task 8: Create customer 1 Total
customer_one_total = 0

# Task 9: List of items purchasing
customer_one_itemization = ""

# Task 10: Add lovely loveseat price to customer 1 total
customer_one_total += lovely_loveseat_price

# Task 11: Add item to customer 1 list
customer_one_itemization += lovely_loveseat_description

# Task 12: Add luxurious lamp price to customer 1 total
customer_one_total += luxurious_lamp_price

# Task 13: Add item to customer 1 list
customer_one_itemization += luxurious_lamp_description

# Task 14: Calculate customer 1 sales tax
customer_one_tax = customer_one_total * sales_tax

# Task 15: Add sales tax to customer 1 total cost
customer_one_total += customer_one_tax

# Task 16: Begin receipt for customer 1
print("Customer One Items:")

# Task 17: Print list of items
print(customer_one_itemization)

# Task 18: Print heading for total cost
print("Customer One Total:")

# Task 19: Print customer 1 total
print(customer_one_total)

# Task 20: Finish
