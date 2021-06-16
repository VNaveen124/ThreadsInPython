#multable.py
from threading import *
import time
def  multable():
	n=int(input("Enter a number:"))
	if(n<=0):
		print("{} is invalid:".format(n))
	else:
		print("-------------------------------------------------")
		print("Mul Table for:{}".format(n))
		print("-------------------------------------------------")
		for i in range(1,11):
			print("{} x {}={}".format(n,i,n*i))
			time.sleep(0.5)
		print("-------------------------------------------------")
	
#main program
t=Thread(target=multable)
t.start()
