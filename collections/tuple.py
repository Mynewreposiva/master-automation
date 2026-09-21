# tuple () : tuples are immutable, which means once a tuple is created, you cannot remove, add, or change individual elements directly.
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))

# tuple data items
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# tuple constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Update tuple: since tuple immute Convert the tuple into a list to be able to change it:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])


x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# unpack tuples

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# loop: index based
thistuple = ("apple", "banana", "cherry")
count = len(thistuple) # 3 length
print(" loop")
for i in range(count):
    print(thistuple[i])

#direct loop
    thistuple = ("apple", "banana", "cherry")
    for x in thistuple:
        print(x)
# while loop:

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
#   Index 0: "apple"
#   Index 1: "banana"
#   Index 2: "cherry"

# Loop Pass 1: i = 0 -> condition (0 < 3) is True -> prints "apple"  -> i becomes 1
# Loop Pass 2: i = 1 -> condition (1 < 3) is True -> prints "banana" -> i becomes 2
# Loop Pass 3: i = 2 -> condition (2 < 3) is True -> prints "cherry" -> i becomes 3
# Loop Exit:   i = 3 -> condition (3 < 3) is False -> loop terminates

# join tuples

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)