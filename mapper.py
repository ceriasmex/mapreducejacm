#!/usr/bin/python 

import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for words in words:
        print ("Hola" +  words + "Count" + str(1))
        
