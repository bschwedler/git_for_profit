#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

filename = 'HARFIX.txt'
print filename

f = open(filename)
for line in f:
    point_id = line[0:77]
    point_lon = line[78:90]
    point_lat = line[91:104]
    point_type = line[105:106]
    point_class = line[107:118]
    point_pitch = line[119:120]
    point_catch = line[121:122]
    point_way = line[123:124]
    print point_id, point_lon, point_lat, point_type, point_class, \
            point_pitch, point_catch, point_way

f.close()

