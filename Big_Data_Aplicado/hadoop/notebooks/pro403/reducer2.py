#!/usr/bin/env python3

import sys 

for line in sys.stdin:
    ip , val = line.strip().split(" ",1)
    bytes = int(val)

    print(f"{ip}: {bytes} bytes")

