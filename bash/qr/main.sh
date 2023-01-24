#!/bin/bash
colourinit
qr="qrcode.QRCode(version=1, box_size=10, border=4)"
qrdir="./QRs"
if [ ! -d "$qrdir" ]; then
    mkdir $qrdir
else
    echo -e "\033[36m[i] QRs directory already exists, continuing\033
