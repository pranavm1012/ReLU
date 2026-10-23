# q8.py
# Sets & duplicates

# Creating a list with repeated numbers
repeated_numbers = [1, 2, 2, 3, 4, 4, 4, 5]
print("Original list with duplicates:", repeated_numbers)

# Convert into a set
unique_set = set(repeated_numbers)
print("Resulting set (no duplicates):", unique_set)

# Explanation:
# Sets in Python are unordered collections of unique elements.
# When a list is converted to a set, python retains only one instance of each distinct value and automatically removes all duplicate entries.
