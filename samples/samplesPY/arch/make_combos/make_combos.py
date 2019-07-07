
import matplotlib.pyplot as plt
import numpy as np

#the java oscillograph is more correctly a flat torus, I think
####30/12/2015, it works, it fucking works!!!!!!

def rr(size, corners):
	global arr
	global count
	global totalSize

	if(size>1):
		
# 		print("size:\t", size)
		rr(size-1, corners)
		
		tmpCorners = corners[:]
		tmpCorners.append(size)
# 		print("tmpCorners:\t", tmpCorners)
		
		rr(size-1, tmpCorners)
		
	else:
		for i, cor in enumerate(corners):
			arr[count, totalSize-1 - i, i:i+cor] = 1
		# 
			# print("arr = ", arr[count])
		print("corners:\t", corners)	
		# print("count = ",count)
# 		shw(count)
		count=count+1

		arr[count, :, :] = arr[count-1, :, :]
		arr[count, totalSize-1 - len(corners), len(corners)] = 1
		print("corners:\t", corners, "len...corners:\t", len(corners))
		# print("count = ",count)
		# shw(count)
		# print("count = ", count)
		count=count+1

def shw(cnt):
	global arr
	# plt.matshow(arr[cnt, :, :], cnt+1)
	plt.matshow(arr[cnt, :, :], 0)
	# plt.savefig(str(cnt)+'.jpg')
	
	# plt.show()
	# plt.figure()  # plt.close()
#to plot all as sequence on same figure see following
# http://stackoverflow.com/questions/13443474/matplotlib-sequence-of-figures-in-the-same-window

def showResult(arr):
	# f = plt.figure()
	for combo in range(0, len(arr)):
		plt.matshow(arr[combo, :, :], 0)
		# plt.figure()
		# plt.savefig(str(cnt)+'.jpg')
	
		# plt.show(); plt.close()

totalSize=3
arr=np.zeros((pow(2, totalSize), totalSize, totalSize), dtype=np.int)
count=0
rr(totalSize, [])   

# for a in range(len(arr)):
#     print(arr[a])

# oh ya can't just show the final result I think
# showResult(arr)
# plt.show()