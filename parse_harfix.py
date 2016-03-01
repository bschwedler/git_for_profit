#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

filename = 'HARFIX.txt'
print filename

f = open(filename)
for line in f:
    point_id = line[0:77].strip()
    point_lon = line[78:90].strip()
    point_lat = line[91:104].strip()
    point_type = line[105:106].strip()
    point_class = line[107:118].strip()
    point_pitch = line[119:120].strip()
    point_catch = line[121:122].strip()
    point_way = line[123:124].strip()

f.close()

