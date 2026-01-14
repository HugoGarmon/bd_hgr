#!/usr/bin/env python3

import sys

first = True

for line in sys.stdin:

    if first == True:
        first = False
        continue

    line = line.strip().split(",")
    print(f"{line[3]},1")
