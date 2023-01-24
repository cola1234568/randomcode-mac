#!/bin/bash

pip install qrcode numpy colorama

qrdir="./QRs"

if [ ! -d $qrdir ]; then
mkdir $qrdir
echo -e "\033[1;34m[i]\033[0m QRs directory created, continuing"
else
echo -e "\033[1;34m[i]\033[0m QRs directory already exists, continuing"
fi

qrdirList=$(ls $qrdir)

while true; do
read -p "What would you like to put in the QR Code?\n> " content
qr=qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(content)
qr.make()
echo "QR Code: $(np.array(qr.get_matrix()).shape)"
read -p "Would you like to save? (y/n)\n> " saveyn
if [ $saveyn == "y" ] || [ $saveyn == "yes" ]; then
img = qr.make_image(fill_color="white", back_color="black")
i=0
for f in $qrdirList; do
i=$((i+1))
done
read -p "What should be the file name? (QR_name.png)\n(Note: if empty, will use QRs_$i.png instead)\n> " name
nameori=${name:-$i}
fullpath="$qrdir/QR_$nameori.png"
echo "Attempting to save under "$fullpath""
try:
img.save(fullpath)
catch OSError as err:
echo -e "\033[1;31m[E]\033[0m Could not save QR Code as \033[1;36m"$fullpath"\033[0m\n[OSError]: \033[1;31m$err\033[0m"
exit 1
fi
fi
done