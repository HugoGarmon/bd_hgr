#!/usr/bin/env python3
 
import sys
 
first = True
codes = False
 
for line in sys.stdin:
    if first:
        first = False
        continue
 
    fich = line.strip().split(",")
    if len(fich) > 2:
        codes = True
    else:
        codes = False
   
    if codes:
        line = line.strip().split(",")
 
        code = line[2]
        name = line[0]
        print(f"{code}\tA_{name}")
    else:
        line = line.strip().split(";")
 
        code = line[0]
        pib = line[8]
        print(f"{code}\tB_{pib}")
