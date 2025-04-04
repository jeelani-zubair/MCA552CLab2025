# Python Fundamentals Tutorial
# This script introduces basic Python concepts with clear comments

# 1. Variables and Data Types
# Variable dynamic typing, start with _ or letter, Case-sensitive
# Numeric datatypes: Integers (0b, 0o, 0x), Real Numbers, Complex Numbers (2 + 3j)
# String datatypes ' '| " " | """  """
# Boolean datatypes | True, False
# Sequence type: lists (mutable) [] and tuples (immutable) ()
# Mapping type: Dictionary (key-value pairs)
# Set types
# value = None (None literal)
integer_var = 10  # Integer type
float_var = 10.5  # Float type
string_var = "Hello, Python!"  # String type
boolean_var = True  # Boolean type

# Print statements
print("Integer:", integer_var)
print("Float:", float_var)
print("String:", string_var)
print("Boolean:", boolean_var)

# 2. Conditional Statements
if integer_var > 5:
    print("integer_var is greater than 5")
else:
    print("integer_var is not greater than 5")

print("Outside if-else")

# 3. Loops
# For loop
# range(start, stop, step)
# start → (Optional) The number where the sequence begins (default is 0).
# stop → (Required) The number where the sequence stops (excludes this value).
# step → (Optional) The increment (default is 1).

for i in range(2,11,2):  # Loops from 0 to 4
    print("For loop iteration:", i)

# While loop
counter = 0
while counter < 3:
    print("While loop iteration:", counter)
    counter += 1

# 4. Functions
def greet(name):
    """Function to greet a person."""
    return f"Hello, {name}!"

print(greet("Alice"))
# An f-string is a modern and efficient way to format strings in Python.
# It allows you to embed expressions inside string literals by prefixing the string with f or F.

# 5. Lists (Arrays)
numbers = [1,2,3,4,5] # List declaration
print("List Elements:", numbers)
# numbers.append(6)  # Adding an element
numbers.pop()
print("Updated List:", numbers)

# 6. Dictionaries (Key-Value Pairs)
student = {"name": "John", "age": 20, "grade": "A"}
print("Student Info:", student)
print("Student Name:", student["name"])  # Accessing value by key

# 7. File Handling
with open("sample.txt", "w") as file:
    file.write("This is a sample file. We are adding to it")  # Writing to a file

with open("sample.txt", "r") as file:
    content = file.read()  # Reading from a file
    print("File Content:", content)

# 8. Exception Handling
try:
    result = 10 / 1  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution completed.")
