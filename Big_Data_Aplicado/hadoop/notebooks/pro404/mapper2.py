#!/usr/bin/env python3

import sys 
first = True


for line in sys.stdin:
    if first == True:
        first = False
        continue
    
    line = line.strip().split(";")
    
    region_name = line[1]
    total_gdp = float(line[7])

    
    print(f"{region_name}\t{total_gdp}")
