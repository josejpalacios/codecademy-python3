# In Python, we call the order of an element in a list its index.

# Python lists are zero-indexed. This means that the first element in a list has index 0, rather than 1.

# We can select a single element from a list by using square brackets ([]) and the index of the list item.

# Note that when accessing elements of an array, you must use an int as the index. 
# If you use a float, you will get an error.
# This can be especially tricky when using division.

# To solve this problem, you can force the result of your division to be an int by using the int() function. int() takes a number and cuts off the decimal point.

employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']

# 4th index
index4 = employees[4]

# Print the amount of items in employees
print(len(employees))

# IndexError: list index out of range
# print(employees[8])

print(employees[6])
