#!/usr/bin/env python3

import sys 
first = True


for line in sys.stdin:
    if first == True:
        first = False
        continue
    
    line = line.strip().split(";")

    country_name = line[4]
    year = int(line[6])
    total_gdp = float(line[7])

    if year < 2000 or total_gdp <= 0:
        continue
    
    print(f"{country_name}\t{year}\t{total_gdp}")
