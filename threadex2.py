#threadex2.py
import time
import threading
def   squares (lst): # lst=[10,20,30]
	for n in lst:
		print("Square of {}={}".format(n, n**2) )
		time.sleep(1)

def   cubes (lst): # lst=[10,20,30]
	for n in lst:
		print("cube of {}={}".format(n, n**3) )
		time.sleep(1)

#main program
bt=time.time()
lst=[3,4,5,6,7,8,9]
#create 2 child threads
t1=threading.Thread(target=squares , args=(lst,) )
t2=threading.Thread(target=cubes , args=(lst,) )
#dispatch the child threds
t1.start()
t2.start()
t1.join()
t2.join()
et=time.time()
print("time taken by thread based application=",(et-bt))
