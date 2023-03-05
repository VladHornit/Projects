#  Coin Flip Simulation

import random
length = []
def flip(x,y):
    chain = ""
    while (True):
        x = random.randint(x,y)
        if x == 0:
            chain += "O"
        else:
            chain += "R"
        n = len(chain)
        if n >= 3:
            if chain[n-1] == chain[n-2] and chain[n-1] == chain[n-3]:
                break
    return chain

for i in range(10):
    result = (flip(0,1))
    print(result)
    a = len(result)
    length.append(a)
    print("For getting the result", len(result), "flips were needed")

print(length)
avarege = sum(length)/len(length)
print("Avarege number of flips needed", avarege)
