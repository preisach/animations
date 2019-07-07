#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 18:47:31 2019

@author: m

for musical dimensions
listen bach 
time 32.56
podcast
BBC all in the mind 28.05.19 21:30
http://open.live.bbc.co.uk/mediaselector/6/redir/version/2.0/mediaset/audio-nondrm-download/proto/http/vpid/p07bkkr0.mp3

"""

import matplotlib.pyplot as plt
import subprocess as sp
# import re as re;
# import string
# import sys
    
import json

def doTheBiz(out, o2):    
# def doTheBiz(out):
    # fig = plt.figure(figsize=(4, 4))
    plt.plot([-0.1, 1.1], [-0.1,1.1], color='w', linewidth=0)
    x = []
    y = [] 
    
    
    lines = o2.strip('\n').split('\n')
    for line in lines:
    # jso = json.loads(out)
    # print(jso)
    
        t1, t2, t3 = [round(float(z), 3) for z in line.split(' ')]
        x = [t1, t2]
        y = [t3, t3]
        # print("x = ", x)    # print("y = ", y)
        plt.plot(x, y, c='blue')
    
    
    lines = out.strip('\n').split('\n')
    for line in lines:
    # jso = json.loads(out)
    # print(jso)
    
        t1, t2, t3 = [round(float(z), 3) for z in line.split(' ')]
        x = [t1, t2]
        y = [t3, t3]
        # print("x = ", x)    # print("y = ", y)
        plt.plot(x, y, c='red')
    
    
    plt.xlabel('input', fontsize=16)    
    plt.ylabel('output', fontsize=16)
    # plt.title ('Multistat/discrete Preisach', fontsize=20)
    # plt.title ('Bistat/Thermostat/Nonideal Relay\nHysteron', fontsize=24)
    
    
    plt.show()
    # # If you save the plot as an image you can set the background 
    # # to be transparent
    # # myploy.savefig('plotname.png', transparent=True)

out = ""
try:
    out = sp.check_output(["node", "/home/m/_portfolio/preisach/preisachjs/samples/printDegaussed.js"]) 
    out = out.decode("utf-8")    
    
    # doTheBiz(out)
    # print("out = ", out)
    try:
        o2 = sp.check_output(["node", "/home/m/_portfolio/preisach/preisachjs/samples/printAllStatios.js"]) 
        o2 = o2.decode("utf-8")    
        # print("out = ", out)
        doTheBiz(out, o2)

    except sp.CalledProcessError as e:
        print("error = ", e)
        # return_code = e.returncode
    

except sp.CalledProcessError as e:
    print("error = ", e)
    # return_code = e.returncode


