#!/usr/bin/env python3

import sys

cont = 0
total = 0
region_actual = None

for line in sys.stdin:
    line = line.strip().split()

    region = line[0]
    gdp = float(line[1])

    if region_actual == None:
        region_actual = region

    if region != region_actual:
        prom = total / cont 
        print(f"{region_actual}  {prom}")
        
        region_actual = region
        total = gdp    
        cont = 1

    if region_actual == region:
        total = total + gdp
        cont = cont + 1 

if region_actual is not None:
    prom = total / cont
    print(f"{region_actual}\t{prom}")
