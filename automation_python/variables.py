# Variables are used to store data that can be referenced and manipulated during program execution
# A variable is essentially a name that is assigned to a value.

x = 5
name = "Alex"
print(x)
print(name)

# valid
age = 21
_colour = "lilac"
total_score = 90

print(age)
print(_colour)
print(total_score)

# bad variables
# 1name = "Error"   # Starts with a digit
# class = 10        # class is a reserved keyword
# user-name = "Doe" # Contains a hyphen"""

# Dynamic Typing:  same variable can store different data types.
# It stores the latest value you assigned to it, and it completely forgets the previous value and type.
x = 10
x = "Now a string"

print(x) # Result is "Now a string"


# Assigning Same Value: =
a = b = c = 100
print(a, b, c)

# Assigning Different Values: ,
x, y, z = 1, 2.5, "Python"
print(x, "," , y, "," , z)

# deleting a variable

x = 10
del x
print(x)