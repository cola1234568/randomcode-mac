import os
import random
from time import sleep

path = input("where do you want to risk?\nplease use forward slashes (/) and not backslashes (\\).\n> ")

a = True
while a:
    try:
        pathlist = os.listdir(path)
        a = False
    except OSError:
        path = input(f"{path} doesn't exist.\nplease choose a valid path\n(make sure it is the whole path (including C:\ for windows))\n> ")

print(pathlist)
file = random.choice(pathlist)

shoot = input("press enter to shoot")
if len(shoot) != 0:
    b = False
    print("then what was the point of opening this file???")
    sleep(2)
    print("i'm leaving")
    sleep(2)
    exit()
else:
    b = True

while b:
    pathlist = os.listdir(path)
    if random.randint(0, 6) == 2:
        print(f"unlucky...deleting {file}")
        os.remove(f"{path}\{file}")
    else:
        print("safe")
    shoot = input("shoot again? (press enter to shoot)")
    if len(shoot) != 0:
        b = False

# needs to be checked for bugs, can you help :D