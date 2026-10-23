# q7.py
# List vs Tuple

# List and tuple with the same 4 elements
my_list = [10, 20, 30, 40]
my_tuple = (10, 20, 30, 40)

print("Original list: ", my_list)
print("Original tuple:", my_tuple)

# 1. Modifying the list (Lists are mutable)
my_list[0] = 99
print("\nModified list:", my_list)
print("-> Lists are mutable, so elements can be updated in-place.")

# 2. Modifying the tuple (Tuples are immutable)
try:
    my_tuple[0] = 99
except TypeError as error:
    print(f"\nWhat happens when modifying a tuple(The error message we get): {error}")
    print("-> Tuples are immutable, so updating elements in-place raises a TypeError.")

# Explanation:
# Lists in Python are mutable objects (stored as dynamic arrays), allowing in-place insertion, deletion, and reassignment.
# Tuples are immutable objects, designed to maintain fixed, write-protected collections. Once created, their elements cannot be changed.
