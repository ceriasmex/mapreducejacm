#!/usr/bin/python 

import sys

for line in sys.stdin:
    line = line.strip()
    print("Sera hola??")
    if line == "Hola":
        print ("no es hola")
    