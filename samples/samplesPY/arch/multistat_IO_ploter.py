#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 09:19:36 2019

@author: m
"""

import matplotlib.pyplot as plt
import subprocess as sp
# from subprocess import call
# from subprocess import check_output

# Note that you have to specify path to script
# check_output
out = ""
try:
    out = sp.check_output(["node", "/home/m/_portfolio/preisach/preisachjs/testPreisach.js"]) 
    # out = out.decode("utf-8")
    # print("out = ", out)
except sp.CalledProcessError as e:
    print("error = ", e)
    return_code = e.returncode

# print(out)
# print(out[0])
x = []
y = [] 
# x[0] = 0
# x[1] = 0
# y[0] = 0
# y[1] = 0
fig = plt.figure(figsize=(4, 4))
plt.plot([-0.1, 1.1],        [-0.2,1.2], color='w', linewidth=0)
statios = []
out = out.strip('\n')
statios = out.split('\n')
# print("statios = ", statios)
# print("statios.length = ", len(statios))
for statio in statios:
    # print("statio = ", statio)
    # print("statio.length = ", len(statio))
    # [x[0], x[1], y[0], y[1]] = statio.split(' ')
    nums = [round(float(z), 3) for z in statio.split(' ')]
    # print("nums = ", nums)
    x = [nums[0], nums[1]]
    y = [nums[2], nums[3]]
    print(nums)
    # print("x = ", x)
    # print("y = ", y)
    # print(x, y, c='b')
    plt.plot(x, y, c='b')

plt.xlabel('input', fontsize=16)    
plt.ylabel('output', fontsize=16)
plt.title ('Bistat/Thermostat/Nonideal Relay - Hysteron', fontsize=0)

plt.show()
    


