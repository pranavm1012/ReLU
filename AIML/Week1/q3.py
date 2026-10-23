# q3.py
# Taking input from user and type conversion from string to 
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Arithmetic operations
sum_value = num1 + num2
diff_value = num1 - num2
prod_value = num1 * num2

# Division (setting denominator !=0 condition)
quot_value = num1 / num2 if num2 != 0 else "Undefined (Denominator should not be zero)"

# Displaying results
print(f"Sum: {sum_value}")
print(f"Difference: {diff_value}")
print(f"Product: {prod_value}")
print(f"Quotient: {quot_value}")
