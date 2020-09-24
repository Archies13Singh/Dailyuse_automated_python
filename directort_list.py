#!/usr/bin/env python3
import os

dirc =input("Enter the directory name : ")
for name in os.listdir(dirc):
    fullname = os.path.join(dirc,name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))


