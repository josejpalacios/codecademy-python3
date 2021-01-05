# Polymorphism is the term used to describe the same syntax (like the + operator here,
# but it could be a method name) doing different actions depending on the type of data.

# Polymorphism is an abstract concept that covers a lot of ground,
# but defining class hierarchies that all implement the same interface is a way of
# introducing polymorphism to our code.

a_list = [1, 18, 32, 12]
a_dict = {'value': True}
a_string = "Polymorphism is cool!"
# Call len on each variable. Print results.
print(len(a_list))
print(len(a_dict))
print(len(a_string))
# len is different for each because:
# len counts the number of items in a list
# Len counts the number of key value pairs in a dictionary
# len counts the number of characters in a string

# len is similar because it is count information stored in the variables
