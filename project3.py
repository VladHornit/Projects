# Roulette Game

import random

print("""This is the Roulette game, you can make bet in the next order:
> Single number (1 to 36, 0,)
> Red versus Black
Red: 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30 32, 34, 36
Black: 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35
> Odd versus Even (Note that 0 and 00 do not pay out for even)
> 1 to 18 (enter 'first half') versus 19 to 36 (enter 'second half')""")

bet = input("Please, make your bet >>> ")
r = random.randint(0, 37)
print("The winning number is: ", r)

if bet == str(r):
    print( "Your 'Single number' bet won! Our congratiulatins!")

elif (bet == "Red" or bet == "red") and (r == 1 or r == 3 or r == 5 or r == 7 \
or r == 9 or r == 12 or r == 14 or r == 16 or r == 18 or r == 19 or r == 21 or r == 23 \
or r == 25 or r == 27 or r == 32 or r == 34 or r == 36):
    print("Your 'Red' bet won! Our congratiulatins!")

elif (bet == "Black" or bet == "black") and (r == 2 or r == 4 or r == 6 or r == 8 \
or r == 10 or r == 11 or r == 13 or r == 15 or r == 17 or r == 20 or r == 22 or r == 24 \
or r == 26 or r == 28 or r == 29 or r == 31 or r == 33 or r == 35):
    print("Your 'Black' bet won! Our congratiulatins!")

elif (bet == "Odd" or bet == "odd") and r % 2 != 0:
    print("Your 'Odd' bet won! Our congratiulatins!")

elif (bet == "Even" or bet == "even") and r % 2 == 0:
    print("Your 'Even' bet won! Our congratiulatins!")

elif (bet == "First half" or bet == "first half") and 1 <= r <= 18:
    print("Your bet '1-18' won! Our congratiulatins!")

elif (bet == "Second half" or bet == "second half") and r >= 36:
    print("Your bet '1-18' won! Our congratiulatins!")

elif bet == r and r == 0:
    print(" Your bet '0 - ZERO' won! Our congratiulatins!")

else:
    ("Please, make corect bet. Check for the example.")
