#threadex5.py
import time
from threading import*
class Kvr:		#without Inheritance
	def   show(self):
		for i in range(5):
			print("i am child thread")
			time.sleep(2)




#main program
k=Kvr()
t=Thread(target=k.show)
t.start()
