#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

ary=[1,3,4,6,8]
for i in ary:
    if i==4:
        print("find 4!")
#        break
        continue
    print(i)
else:
    print("END!")

for ii in range(1,20,2):
    print(ii)