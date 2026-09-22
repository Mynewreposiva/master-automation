#1 IF
age =int(input("Enter your age in if condition: "))
if age>18:
     print(" eligible")

#2 If else Statement
agecount = int(input("Enter your age in if else condition: "))
if agecount <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")

#3 If-elif-else Statement
realage=int(input("Enter your age in if elseif else: "))
if realage <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")
# programme 2
# Get the day of the week from the user
day = input("Enter a day of the week: ").strip().lower()

# Check the day and print the matching activity

if day == "sunday":
    print("It's Sunday! Time for playing!")
elif day == "monday":
    print("It's Monday. Back to work or study.")
elif day == "tuesday":
    print("It's Tuesday. Keep grinding!")
elif day == "wednesday":
    print("It's Wednesday. Hump day, you are halfway there!")
elif day == "thursday":
    print("It's Thursday. Just one more day until the weekend!")
elif day == "friday":
    print("It's Friday! Weekend is almost here, time for a movie night!")
elif day == "saturday":
    print("It's Saturday! Time for shopping and relaxing.")
else:
    print("That is not a valid day of the week. Please check your spelling.")

#4 Nested if-else Statement
age2 = int(input("Enter age in nested if "))
is_member = True

if age2 >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")
