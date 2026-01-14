#!/usr/bin/env python3

import sys 

cat_act = None
total = 0

for line in sys.stdin:
    line = line.strip().split("\t")

    cat = line[0]
    val = int(line[1])

    if cat_act == None:
        cat_act = cat
    
    if cat_act == cat:
        total = total + val

    if cat_act != cat:
        print(f"{cat_act} {total}")
        cat_act = cat 
        total = val
    
print(f"{cat_act} {total}")    
