# Create a tuple containing two numbers
n1 = (20, 30)

# This creates a tuple: (30, 5)
n2 = 10 + 20, 5

# Concatenate n1 and n2:
number = (n1 + n2,)

# Tuples cannot be changed after creation (immutable)
# Uncommenting the next line will cause an error
# number[0] = 4

# Tuple unpacking example
# num1, num2 = (5, 10)

# Swapping values using tuple unpacking
# num2, num1 = num1, num2

# Print the tuple
print(number)

 Print the data type of number
print(type(number))

# Print swapped values
print(num1, num2)

# Loop through each item in number
# number contains only one item:
# (20, 30, 30, 5)
# for num in number:
#     print(num)

# Find the number of items in number
# Since number contains one element, length = 1
# length = len(number)

# Initialize counter
# count = 0

# Loop through tuple using index numbers
# while count < length:
#     print(number[count])
#     count = count + 1

