#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

filename = 'HARFIX.txt'
print filename

f = open(filename)
for line in f:
    # Line varible includes newline at the end
    sys.stdout.write(line)

f.close()

