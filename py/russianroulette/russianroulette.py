import os
import random
from time import sleep

path = input("Where do you want to risk?\nPlease use forward slashes (/) and not backslashes (\).\n> ")

def file_set(_path):
    try:
        _path_list = os.listdir(_path)
    except OSError:
        print(f"{_path} doesn't exist.\nPlease choose a valid path")
        exit()
    if len(_path_list) == 0:
        print("No files in the specified directory. Exiting...")
        exit()
    set_file = random.choice(_path_list)
    return set_file

while True:
    path_list = os.listdir(path)
    if len(path_list) == 0:
        print("No files in the specified directory. Exiting...")
        exit()
    else:
        break

file_to_delete = file_set(path)
shoot = input(f"Press enter to shoot {file_to_delete}, or type any letter to quit\n> ")
if len(shoot) != 0:
    print("Exiting...")
    exit()

while True:
    if random.randint(0, 6) == 2:
        print(f"Unlucky...deleting {file_to_delete}")
        os.remove(f"{path}/{file_to_delete}")
    else:
        print("Safe")
    shoot = input("Shoot again? (press enter to shoot, or type any letter to quit)\n> ")
    if len(shoot) != 0:
        print("Exiting...")
        exit()
    file_to_delete = file_set(path)
