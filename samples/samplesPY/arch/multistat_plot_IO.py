#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 09:08:32 2019

@author: m
"""

import matplotlib.pyplot as plt

# fig = plt.figure()
fig = plt.figure(figsize=(6,6))

plt.plot([-0.1, 1.1],        [-0.2,1.2], color='w', linewidth=0)

pairs =[ [ [ 0, 0.5 ], [ 0, 0 ] ],
  [ [ 0.25, 0.75 ], [ 0.3333333333333333, 0.3333333333333333 ] ],
  [ [ 0.25, 0.75 ], [ 0.6666666666666666, 0.6666666666666666 ] ],
  [ [ 0.5, 1 ], [ 1, 1 ] ] ]


for p in pairs:
# 	x = [p[0][0], p[1][0]]
# 	y = [p[0][1], p[1][1]]
# 	plt.plot(p[:][0], p[:][1])
# 	fig = plt.plot(x, y)
	fig = plt.plot(p[0], p[1])

plt.xlabel('input', fontsize=16)    
plt.ylabel('output', fontsize=16)
plt.title ('', fontsize=0)

plt.show(fig)   