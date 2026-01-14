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
    variation = float(line[9])

    yearVariation = f"{year}"+","+f"{variation}"

    print(f"{country_name}\t{yearVariation}")
