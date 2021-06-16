#activethreadex.py
import threading,time
def show():
	print("i am from show started execution.....")
	print("Name of child thread=", threading.currentThread().getName())
	time.sleep(10)
	print("i am from show ended execution.....")


t1=threading.Thread(target=show)
t1.start()
print("i am from python main program")
print("Name of main thread=", threading.currentThread().getName())
print("no. of active threads=",threading.activeCount())
t1.join()
print("no. of active threads=",threading.activeCount())
