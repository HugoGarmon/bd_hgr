#!/usr/bin/env python3
import sys
 
first = True

for line in sys.stdin:
    
    if first == True:
        first = False
        continue
    
    line = line.strip()
    words = line.split()
    for word in words:
        print(f"{word}\t1")
