# Errors

#Ex 1 syntax
x = 10
if x > 5:
    print("x is greater than 5")

# Ex 2 runtime
''' 
Division by zero
Accessing an undefined variable
Calling a method on an object that does not exist
File I/O errors
'''
a = 10
b = 0
result = a / b

# Ex 3 Logic
x = 10
y = 5
result = x - y * 2

# How to handle the errors
'''
ValueError: Raised when a function receives an argument of the correct type but an inappropriate value, division by 0
TypeError: Raised when an operation or function is applied to an object of inappropriate type, a + 2
IndexError: Raised when trying to access an index that is out of range in a list or tuple, index (1, 9) in the vector (1, 2, 3)
KeyError: Raised when trying to access a key in a dictionary that doesn’t exist, trivial
'''
# Method 0 
print() # and read error messages carefully, check documentation and google

# Method 1
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number!")

x = 5
assert x > 0, "x should be greater than 0"
''' 
An assertion is a sanity check to test whether 
a condition is true. If the condition is false, 
the program raises an AssertionError.
'''

# Method 2
# Unit test

# Method 3
# Debugging in pythin+