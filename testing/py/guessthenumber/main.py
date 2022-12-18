from random import randint

numrange = input("Range?\n> ")

while type(numrange) != int:
    try:
        numrange = int(numrange)
    except ValueError:
        numrange = input("Please insert a number")

cnum = randint(1, numrange)
pnum = input(f"Select a number between 1 and {numrange}\n> ")

if pnum == cnum:
    print("Nice! you got it right!")
else:
    print(f"Incorrect! The number was {cnum}")
