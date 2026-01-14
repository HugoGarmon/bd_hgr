#!/usr/bin/env python3

import sys 
first = True


for line in sys.stdin:
    if first == True:
        first = False
        continue
    
    line = line.strip().split(";")

    million_gdp = float(line[8])

    if million_gdp < 10000:
        print(f"Economía Pequeña\t1")
    elif million_gdp < 100000:
        print(f"Economía Mediana\t1")
    else:
        print(f"Economía Grande\t1")
    
