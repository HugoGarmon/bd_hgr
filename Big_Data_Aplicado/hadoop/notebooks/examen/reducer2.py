#!/usr/bin/env python3

pelimax = " "
valmax = 0

import sys

for line in sys.stdin:

    val , resto = line.strip().split(",",1)
    val = int(val)
    
    if val > valmax:
        pelimax = resto
        valmax = val

print(f"{valmax},{pelimax}")
