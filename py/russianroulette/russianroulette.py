import os
import random
from time import sleep

path = input("where do you want to risk?\nplease use forward slashes (/) and not backslashes (\\).\n> ")


def file_set():
    _path_list = os.listdir(path)
    if len(_path_list) == 0:
        print("no files in the specified directory. exiting...")
        exit()
    set_file = random.choice(_path_list)
    return set_file


a = True
while a:
    try:
        path_list = os.listdir(path)
        a = False
    except OSError:
        path = input(f"{path} doesn't exist.\nplease choose a valid path\n(make sure it is the whole path "
                     f"(including C:\\ for windows))\n> ")

print(path_list)  # noqa
file_set()

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
    file = file_set()
    if random.randint(0, 6) == 2:
        print(f"unlucky...deleting {file}")
        os.remove(f"{path}\\{file}")
    else:
        print("safe")
    shoot = input("shoot again? (press enter to shoot)")
    if len(shoot) != 0:
        b = False
