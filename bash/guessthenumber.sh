#!/bin/bash

echo "Range?"
read numrange

while ! [[ $numrange =~ ^[0-9]+$ ]]
do
echo "Please insert a number"
read numrange
done

cnum=$((RANDOM % numrange + 1))
echo "Select a number between 1 and $numrange"
read pnum

if [ $pnum -eq $cnum ]; then
echo "Nice! you got it right!"
else
echo "Incorrect! The number was $cnum"
fi
