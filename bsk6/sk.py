#!/usr/bin/python3

import os

f = open("secret.txt", "r")
test = f.readline()

os.remove("secret.txt")

while True:
    pass