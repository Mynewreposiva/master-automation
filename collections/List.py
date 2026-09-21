# Lists []

"""List is a  collection which is ordered and changeable. Allows duplicate members.
   Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
   Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
   Dictionary is a collection which is ordered** and changeable. No duplicate members."""

thislist = ["apple", "banana", "cherry"]
print(thislist)

# List length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# Access list items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Negative Indexing
# -1 refers to the last item, -2 refers to the second last item etc.
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Range of Indexes- Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# nagative range
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# check one item is exist or not
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


  # Change list item
  thislist = ["apple", "banana", "cherry"]
  thislist[1] = "blackcurrant"
  print(thislist)

  # Change range of items
  thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
  thislist[1:3] = ["blackcurrant", "watermelon"]
  print(thislist)


  # Add lsit items
  thislist = ["apple", "banana", "cherry"]
  thislist.append("orange")
  print(thislist)

  # Remove lit items
  thislist = ["apple", "banana", "cherry"]
  thislist.remove("banana")
  print(thislist)

  # Pop - The pop() method removes the specified index. If you do not specify the index, the pop() method removes the last item.
  thislist = ["apple", "banana", "cherry"]
  thislist.pop(1)
  print(thislist)

  thislist = ["apple", "banana", "cherry"]
  thislist.pop()
  print(thislist)

  # The del keyword also removes the specified index:
  thislist = ["apple", "banana", "cherry"]
  del thislist[0]
  print(thislist)

  # delete enitre list
  thislist = ["apple", "banana", "cherry"]
  del thislist


