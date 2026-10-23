# q4.py
num = int(input("Enter an integer: "))

# Setting boolean conditions
is_positive = num > 0
is_negative = num < 0
is_even = (num % 2 == 0)
is_odd = (num % 2 != 0)

# Display boolean results
print(f"Number: {num}")
print(f"Is positive? {is_positive}")
print(f"Is negative? {is_negative}")
print(f"Is even?     {is_even}")
print(f"Is odd?      {is_odd}")
