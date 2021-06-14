#nonthreadex1.py
import time
def   squares (lst): # lst=[10,20,30]
	for n in lst:
		print("Square of {}={}".format(n, n**2) )
		time.sleep(1)

def   cubes (lst): # lst=[10,20,30]
	for n in lst:
		print("cube of {}={}".format(n, n**3) )
		time.sleep(1)


bt=time.time()
lst=[3,4,5,6,7,8,9]
cubes(lst)
print("-------------------------------------------")
squares(lst)
print("-------------------------------------------")
et=time.time()
print("Total Time taken by this non-threading Programming=",(et-bt))
print("-------------------------------------------")
