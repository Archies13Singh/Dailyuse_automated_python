#!/usr/bin/env python3
import os
x=(str(input('Enter the old filename -> ' )))
y=(str(input('Enter filename to get new -> ')))
z=os.rename(x,y)
print("old file name is {} and new file name is {} ".format(x,y))


