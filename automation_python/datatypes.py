# Int - value is represented by int class. It contains positive or negative whole numbers
# float
# complex - It stores numbers with real and imaginary parts. For example: 2+3j
a = 5
b = 5.0
c = 2 + 4j

print(type(a))
print(type(b))
print(type(c))


                # String :
# A string is represented using the str class and can be created using single, double or triple quotes.
s = 'Welcome to the Geeks World'
print(s)
print(type(s))

# access string with index
print(s[1])
print(s[-1])

                   # ----------------List-------------:[
# ordered and mutable collections used to store multiple items in a single variable.
# Elements in a list can be of different data types and are accessed using indexing.
# allow duplicate values.
print("List")
a = [1, 2, 3]
print(a)

b = ["Geeks", "For", "Geeks", 4, 5]
print(b[3])
print(b[-3]) # nagative index starts from -1 from last like -1,-2,-3,-4 so -3 is Geeks



                  #---------------- Tuple-------------- (
# tuple are ordered and immutable collections used to store multiple items in a single variable.
# Once created, tuple elements cannot be modified and are accessed using indexing.
# allow duplicate values:
#  tuple with a single element must include a trailing comma, otherwise Python treats it as a normal value instead of a tuple
print("Tuple:")
t1 = (1,)
print(type(t1))

t2 = ('Geeks', 'For', 'Geeks', 1, 2)
print(t2[3])
print(t2[-3])

#Boolean
print("Boolean:")
print(type(True))
print(type(False))

#------------------Set--------: A set is a collection which is unordered, unchangeable*, and unindexed.

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

  # add set
  thisset = {"apple", "banana", "cherry"}

  thisset.add("orange")

  print(thisset)

    # --------------------Dictionary -----------------------
 #>>>> # Dictionary - A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
              # Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
  thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964,
      "brand": "Ford",
  }
  print(thisdict)