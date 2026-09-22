# For

a = ["geeks", "for", "geeks"]
for idx in range(len(a)):
    print(a[idx])

# While Loop
cnt = 0
while (cnt < 3):
    print("Hello Geek")
    cnt = cnt + 1
# Infinite While Loop
while (True):
    print("Hello Geek")
    break
 # nested for loop
for i in range(1, 5):
    for j in range(i):
     print(i, end=' ')
    print()

    # Outer loop: controls the current row number (i will be 1, 2, 3, then 4)
   # for i in range(1, 5):

        # Inner loop: controls how many times to print 'i' on the current row
       #  for j in range(i):
            # Because i changes on each row, range(i) changes too:
            # - When i = 1: range(1) runs 1 time  (j = 0)
            # - When i = 2: range(2) runs 2 times (j = 0, then j = 1)
            # - When i = 3: range(3) runs 3 times (j = 0, 1, 2)
            # - When i = 4: range(4) runs 4 times (j = 0, 1, 2, 3)

            # Prints the value of 'i' on the same line with a space after it
          #  print(i, end=' ')

        # The inner loop finishes all its passes for this row

        # Moves the cursor to a new line before the outer loop starts the next row
        #print()

print(" 100 values")
x = 0
while x < 100:
    print(x, end=" ")
    x += 2
print("\n value is ", x) # outside loop  printing

# By default, Python's print() function has end="\n" built into it behind the scenes (\n is the symbol for a new line).
    # So whenever you call print(x) without specifying end:
    #   1. It prints the value of x.
    #   2. It automatically presses "Enter" (moves the cursor to the next line).
    #
    # When you write print(x, end=" "), you are overriding that default \n with a space,
    # telling Python: "Don't press Enter—just put a space and stay on the same line."