#!/usr/bin/env python3

import sys

for line in sys.stdin:    
    word, val = line.strip().split(",",1)
    val = int(val)

    val = f"{val:04d}"

    print(f"{val},{word}")
