import qrcode
import numpy as np
import os
from colorama import init as colourinit, Fore
colourinit()
qr = qrcode.QRCode(version=1, box_size=10, border=4)

# make qr dir for when the user wants to save one
qrdir = "./QRs"
try:
    os.mkdir(qrdir)
except FileExistsError:
    print(f"{Fore.CYAN}[i] QRs directory already exists, continuing{Fore.RESET}")
except OSError as err:
    print(f"{Fore.RED}[E]{Fore.RESET} QRs directory cannot be created! Exiting\n{Fore.RED}[OSError]: {err}")
    exit(1)

qrdirList = os.listdir(qrdir)

while True:
    content = input("What would you like to put in the QR Code?\n> ")
    qr.add_data(content)
    qr.make()
    print("QR Code:", np.array(qr.get_matrix()).shape)
    saveyn = input("Would you like to save? (y/n)\n> ").lower()
    if saveyn == ('y' or 'yes'):
        img = qr.make_image(fill_color="white", back_color="black")
        i = 0
        for f in qrdirList:
            i += 1
        name = input(f"What should be the file name? (QR_name.png)\n"
                     f"(Note: if empty, will use QRs_{i}.png instead)\n> ")
        nameori = name if name != '' else i
        fullpath = f"{qrdir}/QR_{nameori}.png"
        print(f"Attempting to save under \"{fullpath}\"")
        try:
            img.save(fullpath)
        except OSError as err:
            print(f"{Fore.RED}[E]{Fore.RESET} Could not save QR Code as {Fore.LIGHTBLUE_EX}\"{fullpath}\"{Fore.RESET}\n"
                  f"[OSError]: {Fore.RED}{err}{Fore.RESET}")
            exit(1)

# todo: refine this if you want. i know i'm not going to.
