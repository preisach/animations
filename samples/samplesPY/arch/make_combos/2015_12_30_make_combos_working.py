
import matplotlib.pyplot as plt
import numpy as np


####30/12/2015, it works, it fucking works!!!!!!

def rr(size, corners):
	global arr
	global count
	global totalSize

	if(size>1):
		rr(size-1, corners)
		tmpCorners = corners[:]
		tmpCorners.append(size)
#        print "corners:\t"+str(tmpCorners)
		rr(size-1, tmpCorners)
	else:
		for i, cor in enumerate(corners):
			print "row:",i, "col: ", cor
			arr[count, totalSize-1 - i, i:i+cor]=1
		print "corners:\t", corners
		shw(count)
		count=count+1
		print "count = ",count

		print "corners:\t", corners
		arr[count, :, :] = arr[count-1, :, :]
		arr[count, totalSize-1 - len(corners), len(corners)]=1
		shw(count)
		count=count+1
		print "count = ",count

def shw(cnt):
	global arr
	plt.matshow(arr[cnt, :, :])
	plt.show()
	plt.close()

totalSize=6
arr=np.zeros((pow(2, totalSize), totalSize, totalSize), dtype=np.int)
count=0
#corners=[]
rr(totalSize, [])   

	
