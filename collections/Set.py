# Set - A set is a collection which is unordered, unchangeable*, and unindexed.

thisset = {"apple", "banana", "cherry"}
print(thisset)

# The set() Constructor - Using the set() constructor to make a set:

# 1. Creating an empty set
empty_set = set()
print(type(empty_set))  # Output: <class 'set'>

# 2. Converting a list with duplicates to unique elements
numbers_list = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers_list)
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}

# 3. Converting a string into a set of characters
word_set = set("hello")
print(word_set)  # Output: {'h', 'e', 'l', 'o'} (Order may vary)


# 4. Converting a dictionary (extracts only the keys)
demo_dict = {'a': 1, 'b': 2}
dict_set = set(demo_dict)
print(dict_set)  # Output: {'a', 'b'}