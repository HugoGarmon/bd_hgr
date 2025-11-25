#!/usr/bin/env python3

import sys

region_actual = None
max_temp = -10000000000
min_temp = 10000000000

for line in sys.stdin:
    line = line.split('\t',1)
    region = line[0]
    temp = float(line[1])

    if region_actual is None:
        region_actual = region
    
    if temp >= max_temp:
        max_temp = temp
    
    if temp < min_temp:
        min_temp = temp

    if region_actual != region:
        print(f"{region_actual} temperatura máxima {max_temp}, temperatura mínima {min_temp}")
        region_actual = region
        max_temp = -10000000000
        min_temp = 10000000000
