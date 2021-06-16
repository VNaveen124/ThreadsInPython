#joinex.py
import threading,time
def emp():
	print("employee started working .....")
	time.sleep(10)
	print("employee stopped working...")

#main program
print("Office Opend by main thread")
t1=threading.Thread(target=emp)
t1.start()

t1.join()
print("Office Closed")
