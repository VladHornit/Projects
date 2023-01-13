month = input("Enter the month of your birth:")
date = int(input("Enter date of your birth:"))
if (month ==  "December" or month ==  "december" and date >= 22) or (month ==  "January" or month ==  "january" and date <= 19):
    print("Zodiac Sign is Capricorn.")
    if month ==  "December" or month ==  "december" and date > 31:
        print("December has 31 day.")

elif (month ==  "January" or month ==  "january" and date >= 20) or (month ==  "February" or month ==  "february" and date <= 18):
    print("Zodiac Sign is Aquarius.")
    if month ==  "January" or month ==  "january" and date > 31:
        print("January has 31 day.")

elif (month ==  "February" or month ==  "february" and date >= 19) or ( month ==  "March" or month ==  "march" and date <= 20):
    print("Zodiac Sign is Pisces.")
    if month ==  "February" or month ==  "february" and date > 29:
        print("February has 28/29 day.")

elif (month ==  "March" or month ==  "march" and date >= 21) or ( month ==  "April" or month ==  "april" and date <= 19):
    print("Zodiac Sign is Aries.")
    if month ==  "March" or month ==  "march" and date > 31:
        print("March has 31 day.")

elif (month ==  "April" or month ==  "april" and date >= 20) or ( month ==  "May" or month ==  "may" and date <= 20):
    print("Zodiac Sign is Taurus.")
    if month ==  "April" or month ==  "april" and date > 30:
        print("April has 30 day.")

elif (month ==  "May" or month ==  "may" and date >= 21) or ( month ==  "June" or month ==  "june" and date <= 20):
    print("Zodiac Sign is Gemini.")
    if month ==  "May" or month ==  "may" and date > 31:
        print("May has 31 day.")

elif (month ==  "June" or month ==  "june" and date >= 21) or ( month ==  "July" or month ==  "july" and date <= 22):
    print("Zodiac Sign is Cancer.")
    if month ==  "June" or month ==  "june" and date > 30:
        print("June has 30 day.")

elif (month ==  "July" or month ==  "july" and date >= 23) or ( month ==  "August" or month ==  "august" and date <= 22):
    print("Zodiac Sign is Leo.")
    if month ==  "July" or month ==  "july" and date > 31:
        print("July has 31 day.")

elif (month ==  "August" or month ==  "august" and date >= 23) or ( month ==  "September" or month ==  "september" and date <= 22):
    print("Zodiac Sign is Virgo.")
    if month ==  "August" or month ==  "august" and date > 31:
        print("August has 31 day.")

elif (month ==  "September" or month ==  "september" and date >= 23) or ( month ==  "October" or month ==  "october" and date <= 22):
    print("Zodiac Sign is Libra.")
    if month ==  "September" or month ==  "september" and date > 30:
        print("September has 30 day.")

elif (month ==  "October" or month ==  "october" and date >= 23) or ( month ==  "November" or month ==  "november" and date <= 21):
    print("Zodiac Sign is Scorpio.")
    if month ==  "October" or month ==  "october" and date > 31:
        print("October has 31 day.")

elif (month ==  "November" or month ==  "november" and date >= 22) or ( month ==  "December" or month ==  "december" and date <= 21):
    print("Zodiac Sign is Scorpio.")
    if month ==  "November" or month ==  "november" and date > 30:
        print("November has 30 day.")

else:
    print("Please, enter the correct information.")
