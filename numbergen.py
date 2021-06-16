#numbergen.py
from threading import *
import time
class NumberGen(Thread):
	def  run(self):
		n=int(input("Enter a number:"))
		if(n<=0):
			print("{} is invalid:".format(n))
		else:
			print("-------------------------------------------------")
			print("Numbers within:{}".format(n))
			print("-------------------------------------------------")
			for i in range(1,n+1):
				print("Val of i={}".format(i))
				time.sleep(1)
			print("-------------------------------------------------")
	
#main program
dt=NumberGen()
dt.start()
		
