# ========================
# Make Some Pizzas Section
# ========================
# Task 1: Create list toppings
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

# Task 2: Create list prices
prices = [2, 6, 1, 3, 2, 7, 2]

# Task 3: Get length of toppings
num_pizzas = len(toppings)

# Task 4: Print message
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

# Task 5: Create zip object using prices and toppings. Convert zip to a list.
pizzas = list(zip(prices, toppings))

# Task 6: Print pizzas
print(pizzas)

# ==================================
# Sorting and Slicing Pizzas Section
# ==================================
# Task 7: Sort pizzas
pizzas.sort()

# Task 8: Get first element of pizzas
cheapest_pizza = pizzas[0]

# Task 9: Get last element of pizzas
priciest_pizza = pizzas[-1]

# Task 10: Get first 3 elements of pizzas
three_cheapest = pizzas[:3]

# Task 11: Print three_cheapest
print(three_cheapest)

# Task 12: Count the occurrences of 2 in prices list. Print value.
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
