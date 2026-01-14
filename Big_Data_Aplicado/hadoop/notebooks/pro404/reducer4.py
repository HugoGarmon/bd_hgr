#!/usr/bin/env python3
 
import sys
 
codes = {}
 
for line in sys.stdin:
    line = line.strip().split()
    cod = line[0]
    rest = line[1]
 
    rest = rest.strip().split("_")
    if rest[0] == "A":
        codes[cod] = rest[1]
    elif rest[0] == "B":
        if cod in codes:
            print(f"{codes[cod]}\t{rest[1]}")
