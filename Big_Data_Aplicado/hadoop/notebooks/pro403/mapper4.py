#!/usr/bin/env python3

import sys

for line in sys.stdin:

    line = line.strip().split()
    print(f"{line[5]}, 1")
