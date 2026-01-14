#!/usr/bin/env python3

import sys

first = True


for line in sys.stdin:
    if first == True:
        first = False
        continue
    
    line = line.strip().split(";")

    country_name = line[4]
    income_group = line[5]

    print(f"{income_group}\t{country_name}")

