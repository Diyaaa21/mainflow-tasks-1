# Creating a list
my_list = [1, 2, 3, 4]
print("Original list:", my_list)

# Adding an element to the list
my_list.append(5)
print("List after adding an element:", my_list)

# Removing an element from the list
my_list.remove(3)
print("List after removing an element:", my_list)

# Modifying an element in the list
my_list[1] = 20
print("List after modifying an element:", my_list)

# Creating a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Original dictionary:", my_dict)

# Adding a key-value pair to the dictionary
my_dict['d'] = 4
print("Dictionary after adding a key-value pair:", my_dict)

# Removing a key-value pair from the dictionary
del my_dict['b']
print("Dictionary after removing a key-value pair:", my_dict)

# Modifying a value in the dictionary
my_dict['c'] = 30
print("Dictionary after modifying a value:", my_dict)

# Creating a set
my_set = {1, 2, 3, 4}
print("Original set:", my_set)

# Adding an element to the set
my_set.add(5)
print("Set after adding an element:", my_set)

# Removing an element from the set
my_set.remove(2)
print("Set after removing an element:", my_set)

# Modifying elements in the set (note: sets do not support direct modification of elements)
# We can remove and add elements instead
my_set.discard(3)  # Removes an element if it exists
my_set.add(30)
print("Set after modifying elements:", my_set)
