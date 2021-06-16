#ThreadEx4.py
from threading import *
import time
class Kvr(Thread):		#with Inheritance
	def    run(self):
		 for i in range(1,5):
			 print("i am from child thread")
			 time.sleep(2)


#main program
k=Kvr()
k.start()
