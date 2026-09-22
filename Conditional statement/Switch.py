# Match-Case Statement
number=2
match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")
# program2
day="Monday | Tuesday"
match day:
    case "Sunday":
        print("Sunday")
    case "Monday | Tuesday":
        print("Monday | Tuesday")
