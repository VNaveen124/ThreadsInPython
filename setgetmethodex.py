#setgetmethodex.py
import threading,time
def show():
	print("i am from in show started execution.....")
	ct=threading.currentThread()
	print("Name of child thread=", ct.getName()) #Thread-1
	#change the name of child thread as student
	ct.setName("student")    # (OR)   ct.name="student"
	print("Name of child  thread after changing=",ct.getName())

# main program
t1=threading.Thread(target=show)
t1.start()
mt=threading.currentThread()
print("Name of main thread before changing=",mt.getName())
#change the name of main thread as KVR
mt.setName("KVR")  # (OR) mt.name="KVR"
print("Name of main thread after changing=",mt.getName())
