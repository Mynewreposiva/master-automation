 # 1 Arithmetic Operators

a = 15
b = 4
c=-5
d=2

print("Addition:", a + b)

print("Subtraction:", a - b)

print("Multiplication:", a * b)

print("Division:", a / b)

print("Floor Division:", a // b) #  it returns largest integer less than or equal to the result . it rounds down answer towards negative infinity.

print("Floor Division2:", c // d) # Standard division gives -2.5. but Rounding down (lower value) gives -3 (not -2).
print("Modulus:", a % b) # returns remainder
print("Exponentiation:", a ** b) # 15 by itself 4 times:

# 2. Comparison(or Relational) operators compares values. It either returns True or False according to the condition.

a = 13
b = 33
print("\ncomparison result")
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

# 3 Logical Operators :- Logical AND , OR, NOT
print("\nlogical Operators")
a = True
b = False
print("result is" , a and b)
print("result is" , a or b)
print("result is" , not a)
print(a and b)
print(a or b)
print(not a)

#4 Assignment operators: are used to assign values to the variables
a = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)

#5 Identity Operators:- "is" and "is not" are the identity operators and both are used to check if two values are located on the same part of the memory.

a = 10
b = 20
c = a
print("\nidentify operator")

print(a is not b)
print(a is c)

#6 Membership Operators:- "in" and "not in" are the membership operators that are used to test whether a value or variable is in a sequence.

x = 24
y = 20
my_list = [10, 20, 30, 40, 50]

if (x not in my_list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")


if (y in my_list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")




