# THIS PROGRAM COMPUTE THE NEXT DAY AFTER YOU HAVE ENTERED
print("Enter the date like in this example: 23.04.2022")
day = int(input("Enter date: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

if year == year and month == 12 and day == 31:
    year += 1
    month -= 11
    day -= 30
    print(f"The next day is", day,".",month,".",year)

elif (month == 4 or month == 6 or month == 9 or month == 11) and day <= 29:
    day +=1
    print(f"The next day is", day,".",month,".",year)
elif (month == 4 or month == 6 or month == 9 or month == 11) and day == 30:
    day -= 29
    month += 1
    print(f"The next day is", day,".",month,".",year)

elif (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and day <= 30:
    day +=1
    print(f"The next day is", day,".",month,".",year)
elif (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and day == 31:
    day -= 30
    month += 1
    print(f"The next day is", day,".",month,".",year)

elif month == 2 and day <= 27:
    day +=1
    print(f"The next day is", day,".",month,".",year)
elif month == 2 and day == 28:
    day -= 27
    month += 1
    print(f"The next day is", day,".",month,".",year)

else:
    print("""Plese enter the date like in example.
Or check for the probably mistake in your date
some months have 30 and some 31 days.""")
