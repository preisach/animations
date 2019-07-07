#!/usr/bin/python 

######################################################################
# program called with array.length
######################################################################
import numpy as np

#    this.weight = 1.0/((numGraduations*(numGraduations+1))/2.0);
# weights = function(){
l = 3
q = 1.0/((l*(l+1))/2.0)

min = 0
max = 1
w = np.arange(l, l)
print(w)
# w=np.array([(if(i>j):q;else:0) for i in range(l) for j in range(l) ])
print(w)


# w[] = []
# print range(3:0)
for i in range(l,0):
    print(i)
#     z = []
# #    for j in range(i,l):
#     for j in range(l,0):
#         if j < i: 
#             z.append(0)
#         else:
#             z.append(flatWeight)
#     w.append(z)
# print w


