#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

filename = 'HARFIX.txt'
print filename

point_fields = {
        'id': slice(0, 77),
        'lon': slice(78, 90),
        'lat': slice(91, 104),
        'type': slice(105, 106),
        'class': slice(107, 118),
        'pitch': slice(119, 120),
        'catch': slice(121, 122),
        'way': slice(123, 124),
        }

f = open(filename)
for line in f:
    point_info = {}
    for k, v in point_fields.items():
        point_info[k] = line[v]

f.close()

