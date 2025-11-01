#!/bin/bash
echo "hi! i'm gonna ask your password to install python and pip and then install all the libraries that are missing"
  if command -v apt &> /dev/null;
then sudo apt install python3 python3-pip
elif command -v dnf &> /dev/null;
then sudo dnf install python3 python3-pip
elif command -v yum &> /dev/null;
then sudo yum install python3 python3-pip
elif command -v pacman &> /dev/null;
then sudo pacman -S python python-pip
else read -p "can't find your package manager. i'm no linus torvalds. sorry. press ENTER to exit" && exit
fi

if python3 -m pip &> /dev/null;
then python3 -m pip install pytest requests typing
elif python -m pip &> /dev/null;
then python -m pip install pytest requests typing
else read -p "some problem with pip installation. press ENTER to exit" && exit
fi
echo ''
echo '^_^'
echo ''
read -p "everything's installed, now run run_tests.sh the same way you ran this script. press ENTER to exit and go on"