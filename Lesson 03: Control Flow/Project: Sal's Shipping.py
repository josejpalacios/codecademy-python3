# Task 1: Create function for cost of ground shipping
def cost_ground_shipping(weight):
  # Variable to hold cost
  cost = 0
  # If weight <= 2
  if weight <= 2:
    # Add price per pound
    cost += weight * 1.5
  # Else if weight > 2 and weight <= 6
  elif (weight > 2) and (weight <= 6):
    # Add price per pound
    cost += weight * 3.0
  # Else if weight > 6 and weight <= 10
  elif (weight > 6) and (weight <= 10):
    # Add price per pound
    cost += weight * 4.0
  # Else weight > 10
  else:
    # Add price per pound
    cost += weight * 4.75
  # Add flat charge
  cost += 20
  # Return cost
  return cost

# Task 2: Test function with 8.4. Should cost $53.60
print(cost_ground_shipping(8.4))

# Task 3: Variable for premium ground shipping
premium_ground_shipping = 125.0

# Task 4: Create function for cost of drone shipping
def cost_drone_shipping(weight):
  # Variable to hold cost
  cost = 0
  # If weight <= 2
  if weight <= 2:
    # Add price per pound
    cost += weight * 4.5
  # Else if weight > 2 and weight <= 6
  elif (weight > 2) and (weight <= 6):
    # Add price per pound
    cost += weight * 9.0
  # Else if weight > 6 and weight <= 10
  elif (weight > 6) and (weight <= 10):
    # Add price per pound
    cost += weight * 12.0
  # Else weight > 10
  else:
    # Add price per pound
    cost += weight * 14.20
  # Return cost
  return cost

# Task 5: Test function with 1.5. Should cost $6.75
print(cost_drone_shipping(1.5))

# Task 6: Create function to determine which shipping method is cheapest and how much it will cost
def shipping_method(weight):
  # Determine cost for ground shipping
  ground_shipping = cost_ground_shipping(weight)
  # Determine cost for drone shipping
  drone_shipping = cost_drone_shipping(weight)
  # If ground shipping < drone shipping and ground shipping < premium ground shipping
  if (ground_shipping < drone_shipping) and (ground_shipping < premium_ground_shipping):
    # Print message
    print("The cheapest shipping method is ground shipping. The cost to ship a package that weights " + str(weight) + " lbs using ground shipping is $" + str(ground_shipping) + ".")
  # If drone shipping < ground shipping and drone shipping < premium ground shipping
  elif (drone_shipping < ground_shipping) and (drone_shipping < premium_ground_shipping):
    # Print message
    print("The cheapest shipping method is drone shipping. The cost to ship a package that weights " + str(weight) + " lbs using drone shipping is $" + str(drone_shipping) + ".")
  # Else premium ground shipping < ground shipping and premium ground shipping < drone shipping
  else:
    # Print message
    print("The cheapest shipping method is premium ground shipping. The cost to ship a package that weights " + str(weight) + " lbs using premium ground shipping is $" + str(premium_ground_shipping) + ".")

# Task 7: Test function with 4.8 and 41.5.
shipping_method(4.8)
# The cheapest shipping method is ground shipping. The cost to ship a package that weights 4.8 lbs using ground shipping cost $34.4
shipping_method(41.5)
# The cheapest shipping method is premium ground shipping. The cost to ship a package that weights 41.5 lbs using premium ground shipping is $125.0.
