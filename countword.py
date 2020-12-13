#!/usr/bin/python 

import sys

for line in sys.stdin:
    line = line.strip()
    print("Por fin sin hola")
    if line == "Hola":
        print ("no es hola")
    