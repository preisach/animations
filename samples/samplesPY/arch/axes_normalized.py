#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 12:21:56 2019

@author: m
"""


import matplotlib.pyplot as plt

# fig = plt.figure()
fig = plt.figure(figsize=(6,6))

# want some y padding
# oops there is surely a padding function, anyway, this works
plt.plot([-0.1, 1.1],        [-0.2,1.2], color='w', linewidth=0)

# plt.plot([1.0/3.0, 1.2],     [1.0, 1.0],  color='black', linewidth=4)
# plt.plot([-0.2,    2.0/3.0], [0.0, 0.0],  color='black', linewidth=4)

# plt.plot([1.0/3.0, 1.0/3.0],     [1.0, -0.2], color='grey', linestyle="dashed", linewidth=1)
# plt.plot([2.0/3.0, 2.0/3.0],     [-0.2, 1.0], color='grey', linestyle="dashed", linewidth=1)


plt.plot([0.25, 1.2],     [1.0, 1.0],  color='black', linewidth=4)
plt.plot([-0.2, 0.75],  [0.0, 0.0],  color='black', linewidth=4)

plt.plot([0.25, 0.25],     [1.0, -0.2], color='grey', linestyle="dashed", linewidth=1)
plt.plot([0.75, 0.75],     [-0.2, 1.0], color='grey', linestyle="dashed", linewidth=1)

# plt.plot([1.0/3.0, 1.0/3.0],     [0.0, -0.2], color='grey', linestyle="dashed", linewidth=1)
# plt.plot([2.0/3.0, 2.0/3.0],     [0.0, -0.2], color='grey', linestyle="dashed", linewidth=1)

plt.text(0.28, -0.2, "\u03B1", color="black", fontsize=16)
plt.text(0.78, -0.2, "\u03B2", color="black", fontsize=16)

plt.xlabel('input', fontsize=16)    
plt.ylabel('output', fontsize=16)
plt.title ('Bistat/Thermostat/Nonideal Relay - Hysteron', fontsize=0)

plt.box(True)
plt.savefig("bistat.svg", format="svg", bbox="tight")

# search: dasharray
# replace
# id="line2d_20"
# L 167.049351 \d+
# L 167.049351 420

# <g id="line2d_21">
# <path clip-path="url(#p88fd846fbb)" d="M 275.750649 \d+
# <path clip-path="url(#p88fd846fbb)" d="M 275.750649 420

# 2 occurance
# stroke-linecap:square;stroke-width:4
# stroke-linecap:butt;stroke-width:4