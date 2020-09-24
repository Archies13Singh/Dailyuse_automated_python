#!/usr/bin/env python3
import pandas as pd

x = str(input("Enter the txt format filename :"))
y = str(input("Enter the csv format filename to save :"))

df = pd.read_csv("{}".format(x),delimiter=",")
df.to_csv("{}".format(y))

