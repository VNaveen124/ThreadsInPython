#alive.py
import threading,time
def emp():
	print("employee started working .....")
	print("is emp thread alive?=", threading.currentThread().is_alive()) #true
	time.sleep(10)
	print("employee stopped working...")

#main program
print("Office Opend by main thread")
t1=threading.Thread(target=emp)
t1.start()
print("is main thread alive?=", threading.currentThread().is_alive()) #true
t1.join()
print("is main thread alive?=", threading.currentThread().is_alive())#true
print("is child thread alive?=", t1.is_alive()) #False
print("Office Closed")
